# Copyright (c) Opendatalab. All rights reserved.
import posixpath
from io import BytesIO
from zipfile import BadZipFile, ZIP_DEFLATED, ZipFile, ZipInfo

from loguru import logger
from lxml import etree


PACKAGE_RELATIONSHIPS_NS = (
    "http://schemas.openxmlformats.org/package/2006/relationships"
)
RELATIONSHIP_TAG = f"{{{PACKAGE_RELATIONSHIPS_NS}}}Relationship"


def normalize_docx_package(file_bytes: bytes) -> bytes:
    """在进入 python-docx 前修复 DOCX 包级容错问题。"""
    with ZipFile(BytesIO(file_bytes)) as source:
        loaded_members: list[tuple[ZipInfo, bytes]] = []
        package_members: set[str] = set()
        skipped_members: set[str] = set()
        changed = False

        for info in source.infolist():
            member_data = _read_member_best_effort(source, info)
            if member_data is None:
                skipped_members.add(info.filename)
                changed = True
                continue
            loaded_members.append((info, member_data))
            package_members.add(info.filename)

        rewritten_members: list[tuple[ZipInfo, bytes]] = []
        for info, member_data in loaded_members:
            normalized_data = member_data
            if info.filename.endswith(".rels"):
                normalized_data = _remove_missing_internal_relationships(
                    info.filename,
                    member_data,
                    package_members,
                    skipped_members,
                )
                if normalized_data != member_data:
                    changed = True
            rewritten_members.append((info, normalized_data))

    if not changed:
        return file_bytes

    return _write_package(rewritten_members)


def _read_member_best_effort(source: ZipFile, info: ZipInfo) -> bytes | None:
    """读取 ZIP 成员；损坏的媒体资源可跳过，关键结构成员继续失败。"""
    try:
        return source.read(info.filename)
    except BadZipFile as exc:
        if _is_skippable_corrupt_member(info.filename):
            logger.warning(
                f"Skipping corrupt non-critical DOCX media member {info.filename}: {exc}"
            )
            return None
        raise


def _is_skippable_corrupt_member(filename: str) -> bool:
    """判断损坏成员是否属于可降级丢弃的 DOCX 媒体资源。"""
    return filename.startswith("word/media/")


def _remove_missing_internal_relationships(
    rels_filename: str,
    rels_xml: bytes,
    package_members: set[str],
    skipped_members: set[str],
) -> bytes:
    """删除指向缺失、非法或已跳过成员的关系，避免 python-docx 加载时崩溃。"""
    try:
        parser = etree.XMLParser(resolve_entities=False, remove_blank_text=False)
        root = etree.fromstring(rels_xml, parser)
    except etree.XMLSyntaxError:
        return rels_xml

    removed_count = 0
    for relationship in list(root):
        if (
            relationship.tag != RELATIONSHIP_TAG
            and etree.QName(relationship).localname != "Relationship"
        ):
            continue
        if relationship.get("TargetMode") == "External":
            continue

        resolved_target = _resolve_internal_relationship_target(
            rels_filename,
            relationship.get("Target"),
        )
        if (
            resolved_target is not None
            and resolved_target in package_members
            and resolved_target not in skipped_members
        ):
            continue

        root.remove(relationship)
        removed_count += 1

    if removed_count == 0:
        return rels_xml

    logger.debug(
        "Removed {} broken internal DOCX relationships from {}",
        removed_count,
        rels_filename,
    )
    return etree.tostring(
        root,
        xml_declaration=True,
        encoding="UTF-8",
        standalone="yes",
    )


def _resolve_internal_relationship_target(
    rels_filename: str,
    target: str | None,
) -> str | None:
    """把内部 relationship Target 解析成 ZIP 包内成员路径。"""
    if not target:
        return None

    target = target.replace("\\", "/")
    if target.startswith("/"):
        resolved = posixpath.normpath(target.lstrip("/"))
    else:
        base_dir = _relationship_source_base_dir(rels_filename)
        if base_dir is None:
            return None
        resolved = posixpath.normpath(posixpath.join(base_dir, target))

    if resolved in {"", "."} or resolved.startswith("../"):
        return None
    return resolved


def _relationship_source_base_dir(rels_filename: str) -> str | None:
    """根据 .rels 路径推导源 part 所在目录。"""
    rels_filename = rels_filename.replace("\\", "/")
    if rels_filename == "_rels/.rels":
        return ""

    marker = "/_rels/"
    if marker not in rels_filename:
        return None

    prefix, rels_basename = rels_filename.rsplit(marker, 1)
    if not rels_basename.endswith(".rels"):
        return None

    source_part_name = rels_basename[: -len(".rels")]
    source_part_path = posixpath.normpath(posixpath.join(prefix, source_part_name))
    return posixpath.dirname(source_part_path)


def _write_package(members: list[tuple[ZipInfo, bytes]]) -> bytes:
    """把规范化后的成员重新写成 DOCX ZIP 包，并重新计算 CRC。"""
    output = BytesIO()
    with ZipFile(output, "w", ZIP_DEFLATED) as target:
        for info, member_data in members:
            target.writestr(info, member_data)
    return output.getvalue()
