# Copyright (c) Opendatalab. All rights reserved.
import posixpath
from io import BytesIO
from pathlib import PurePosixPath
from zipfile import BadZipFile, ZIP_DEFLATED, ZipFile, ZipInfo

from loguru import logger
from lxml import etree

from mineru.backend.utils.office_image import create_text_placeholder


PACKAGE_RELATIONSHIPS_NS = (
    "http://schemas.openxmlformats.org/package/2006/relationships"
)
RELATIONSHIP_TAG = f"{{{PACKAGE_RELATIONSHIPS_NS}}}Relationship"
CORRUPT_MEDIA_IMAGE_FORMATS = {
    ".png": "PNG",
    ".jpg": "JPEG",
    ".jpeg": "JPEG",
}


def normalize_docx_package(file_bytes: bytes) -> bytes:
    """在进入 python-docx 前修复 DOCX 包级容错问题。"""
    with ZipFile(BytesIO(file_bytes)) as source:
        loaded_members: list[tuple[ZipInfo, bytes]] = []
        package_members: set[str] = set()
        changed = False

        for info in source.infolist():
            member_data, member_changed = _read_member_best_effort(source, info)
            if member_changed:
                changed = True
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
                )
                if normalized_data != member_data:
                    changed = True
            rewritten_members.append((info, normalized_data))

    if not changed:
        return file_bytes

    return _write_package(rewritten_members)


def _read_member_best_effort(source: ZipFile, info: ZipInfo) -> tuple[bytes, bool]:
    """读取 ZIP 成员；损坏的常见图片资源降级为占位图，关键成员继续失败。"""
    try:
        return source.read(info.filename), False
    except BadZipFile as exc:
        if _is_replaceable_corrupt_media(info.filename):
            logger.warning(
                f"Replacing corrupt DOCX media member {info.filename} with placeholder: {exc}"
            )
            return _create_corrupt_media_placeholder(info.filename), True
        raise


def _is_replaceable_corrupt_media(filename: str) -> bool:
    """判断损坏成员是否属于可用占位图替换的 DOCX 图片资源。"""
    path = PurePosixPath(filename)
    return (
        filename.startswith("word/media/")
        and path.suffix.lower() in CORRUPT_MEDIA_IMAGE_FORMATS
    )


def _create_corrupt_media_placeholder(filename: str) -> bytes:
    """按原媒体扩展名生成损坏图片占位图字节。"""
    suffix = PurePosixPath(filename).suffix.lower()
    image_format = CORRUPT_MEDIA_IMAGE_FORMATS.get(suffix, "PNG")
    placeholder = create_text_placeholder(
        (320, 180),
        [
            "Corrupt image",
            "placeholder",
        ],
    )
    if image_format == "JPEG":
        placeholder = placeholder.convert("RGB")

    output = BytesIO()
    placeholder.save(output, format=image_format)
    return output.getvalue()


def _remove_missing_internal_relationships(
    rels_filename: str,
    rels_xml: bytes,
    package_members: set[str],
) -> bytes:
    """删除指向缺失或非法内部成员的关系，避免 python-docx 加载时崩溃。"""
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
        if resolved_target is not None and resolved_target in package_members:
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
