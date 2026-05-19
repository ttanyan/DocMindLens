# MinerU 接口文档

## 概述

MinerU 是一个强大的文档解析工具，支持将 PDF、图片、Office 文档转换为 Markdown/JSON 格式。提供多种接口方式：CLI 命令行、REST API、MCP 协议和 Web UI。

***

## 一、CLI 命令行接口

### 1.1 基本使用

```bash
mineru -p <input_path> -o <output_dir> [选项]
```

### 1.2 参数说明

| 参数                 | 简写   | 类型   | 必填 | 默认值                | 说明                                 |
| ------------------ | ---- | ---- | -- | ------------------ | ---------------------------------- |
| `--path`           | `-p` | Path | ✅  | -                  | 本地文件路径或目录，支持 PDF、图片、DOCX、PPTX、XLSX |
| `--output`         | `-o` | Path | ✅  | -                  | 输出目录                               |
| `--api-url`        | -    | str  | ❌  | None               | MinerU FastAPI 服务地址                |
| `--method`         | `-m` | str  | ❌  | auto               | 解析方法：`auto`/`txt`/`ocr`            |
| `--backend`        | `-b` | str  | ❌  | hybrid-auto-engine | 解析后端引擎                             |
| `--lang`           | `-l` | str  | ❌  | ch                 | 语言代码                               |
| `--url`            | `-u` | str  | ❌  | None               | 远程服务器地址（用于 http-client 后端）         |
| `--start`          | `-s` | int  | ❌  | 0                  | 起始页码（从0开始）                         |
| `--end`            | `-e` | int  | ❌  | None               | 结束页码                               |
| `--formula`        | `-f` | bool | ❌  | True               | 是否启用公式解析                           |
| `--table`          | `-t` | bool | ❌  | True               | 是否启用表格解析                           |
| `--image-analysis` | -    | bool | ❌  | True               | 是否启用图片/图表分析                        |
| `--version`        | `-v` | -    | ❌  | -                  | 显示版本信息                             |

### 1.3 支持的后端引擎

| 后端                   | 说明           | 依赖要求                  |
| -------------------- | ------------ | --------------------- |
| `pipeline`           | 通用解析模式       | 需要 `mineru[pipeline]` |
| `vlm-auto-engine`    | 本地 VLM 高精度模式 | 需要 `mineru[vlm]`      |
| `vlm-http-client`    | 远程 VLM 客户端   | 无需本地 torch            |
| `hybrid-auto-engine` | 本地混合高精度模式    | 需要 `mineru[core]`     |
| `hybrid-http-client` | 远程混合客户端      | 需要 `mineru[pipeline]` |

### 1.4 支持的语言代码

| 代码            | 语言      |
| ------------- | ------- |
| `ch`          | 中文      |
| `ch_server`   | 中文（服务端） |
| `ch_lite`     | 中文（轻量版） |
| `en`          | 英文      |
| `korean`      | 韩语      |
| `japan`       | 日语      |
| `chinese_cht` | 繁体中文    |
| `ta`          | 泰米尔语    |
| `te`          | 泰卢固语    |
| `ka`          | 卡纳达语    |
| `th`          | 泰语      |
| `el`          | 希腊语     |
| `latin`       | 拉丁语     |
| `arabic`      | 阿拉伯语    |
| `east_slavic` | 东斯拉夫语   |
| `cyrillic`    | 西里尔语    |
| `devanagari`  | 天城文     |

### 1.5 使用示例

```bash
# 基本用法
mineru -p ./docs/sample.pdf -o ./output

# 指定后端和语言
mineru -p ./docs/sample.pdf -o ./output -b pipeline -l en

# 解析页码范围
mineru -p ./docs/sample.pdf -o ./output -s 0 -e 10

# 使用远程服务
mineru -p ./docs/sample.pdf -o ./output -b vlm-http-client -u http://127.0.0.1:30000
```

***

## 二、REST API 接口

### 2.1 启动服务

```bash
mineru-api [--host HOST] [--port PORT]
```

默认地址：`http://127.0.0.1:8000`

### 2.2 API 端点列表

| 方法   | 端点                        | 说明     |
| ---- | ------------------------- | ------ |
| POST | `/file_parse`             | 同步解析文件 |
| POST | `/tasks`                  | 异步提交任务 |
| GET  | `/tasks/{task_id}`        | 查询任务状态 |
| GET  | `/tasks/{task_id}/result` | 获取任务结果 |
| GET  | `/health`                 | 健康检查   |

### 2.3 POST /file\_parse（同步解析）

**请求格式：**

```bash
curl -X POST http://127.0.0.1:8000/file_parse \
  -F "files=@sample.pdf" \
  -F "backend=pipeline" \
  -F "lang=ch"
```

**请求参数：**

| 参数                    | 类型   | 必填 | 默认值      | 说明                |
| --------------------- | ---- | -- | -------- | ----------------- |
| `files`               | File | ✅  | -        | 上传的文件（支持多文件）      |
| `backend`             | str  | ❌  | pipeline | 后端引擎              |
| `parse_method`        | str  | ❌  | auto     | 解析方法：auto/txt/ocr |
| `lang`                | str  | ❌  | ch       | 语言代码              |
| `start_page`          | int  | ❌  | 0        | 起始页码              |
| `end_page`            | int  | ❌  | None     | 结束页码              |
| `formula_enable`      | bool | ❌  | true     | 公式解析              |
| `table_enable`        | bool | ❌  | true     | 表格解析              |
| `return_md`           | bool | ❌  | true     | 返回 Markdown       |
| `return_middle_json`  | bool | ❌  | false    | 返回中间 JSON         |
| `return_model_output` | bool | ❌  | false    | 返回模型输出            |
| `return_content_list` | bool | ❌  | false    | 返回内容列表            |
| `return_images`       | bool | ❌  | false    | 返回图片              |
| `response_format_zip` | bool | ❌  | false    | ZIP 格式返回          |

**响应示例：**

```json
{
  "task_id": "abc123",
  "status": "completed",
  "file_names": ["sample"],
  "result": {
    "md": "# 文档标题\n\n正文内容..."
  }
}
```

### 2.4 POST /tasks（异步任务）

**请求格式：**

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -F "files=@sample.pdf" \
  -F "backend=vlm-auto-engine"
```

**响应示例：**

```json
{
  "task_id": "abc123",
  "status": "pending",
  "status_url": "http://127.0.0.1:8000/tasks/abc123",
  "result_url": "http://127.0.0.1:8000/tasks/abc123/result"
}
```

### 2.5 GET /tasks/{task\_id}（查询状态）

**请求格式：**

```bash
curl http://127.0.0.1:8000/tasks/abc123
```

**响应示例：**

```json
{
  "task_id": "abc123",
  "status": "processing",
  "file_names": ["sample"],
  "queued_ahead": 0
}
```

### 2.6 GET /tasks/{task\_id}/result（获取结果）

**请求格式：**

```bash
curl http://127.0.0.1:8000/tasks/abc123/result
```

**响应示例：**

```json
{
  "task_id": "abc123",
  "status": "completed",
  "file_names": ["sample"],
  "result": {
    "md": "# 文档标题\n\n正文内容..."
  }
}
```

### 2.7 GET /health（健康检查）

**请求格式：**

```bash
curl http://127.0.0.1:8000/health
```

**响应示例：**

```json
{
  "status": "healthy",
  "version": "2.5.0",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

***

## 三、MCP 协议接口

### 3.1 启动 MCP 服务

```bash
mineru-mcp
```

或使用 uvx（推荐）：

```bash
uvx mineru-mcp
```

### 3.2 MCP 工具列表

| 工具名称                     | 说明               |
| ------------------------ | ---------------- |
| `parse_document`         | 解析文档文件为 Markdown |
| `get_supported_backends` | 查询支持的后端列表        |

### 3.3 parse\_document 工具

**参数：**

| 参数               | 类型   | 必填 | 默认值          | 说明     |
| ---------------- | ---- | -- | ------------ | ------ |
| `file_path`      | str  | ✅  | -            | 本地文档路径 |
| `output_dir`     | str  | ❌  | 临时目录         | 输出目录   |
| `backend`        | str  | ❌  | pipeline     | 后端引擎   |
| `lang`           | str  | ❌  | auto         | 语言代码   |
| `start_page`     | int  | ❌  | 0            | 起始页码   |
| `end_page`       | int  | ❌  | None         | 结束页码   |
| `formula_enable` | bool | ❌  | true         | 公式解析   |
| `table_enable`   | bool | ❌  | true         | 表格解析   |
| `make_mode`      | str  | ❌  | mm\_markdown | 输出模式   |

**输出模式：**

- `mm_markdown` - MinerU 格式 Markdown（默认）
- `nlp_markdown` - NLP 格式 Markdown
- `content_list` - 内容列表格式
- `content_list_v2` - 内容列表 V2 格式

**使用示例（Cursor/Claude Desktop）：**

```
请使用 MinerU MCP 将以下 URL 的 PDF 文档转换为 Markdown 格式：
https://example.com/sample.pdf
```

```
请使用 MinerU-MCP 将本地的 /path/to/document.pdf 文件转换为 Markdown 格式
```

***

## 四、服务启动命令

### 4.1 核心服务

| 命令              | 说明            |
| --------------- | ------------- |
| `mineru`        | CLI 命令行工具     |
| `mineru-api`    | FastAPI 服务    |
| `mineru-mcp`    | MCP 协议服务      |
| `mineru-gradio` | Gradio Web UI |

### 4.2 模型服务

| 命令                       | 说明            | 依赖                 |
| ------------------------ | ------------- | ------------------ |
| `mineru-vllm-server`     | VLLM 模型服务     | `mineru[vllm]`     |
| `mineru-lmdeploy-server` | LMDeploy 模型服务 | `mineru[lmdeploy]` |
| `mineru-openai-server`   | OpenAI 兼容服务   | `mineru[vlm]`      |

### 4.3 辅助服务

| 命令                       | 说明         |
| ------------------------ | ---------- |
| `mineru-router`          | 路由服务（负载均衡） |
| `mineru-models-download` | 模型下载工具     |

***

## 五、支持的文档类型

| 类型         | 扩展名                                                       | 说明           |
| ---------- | --------------------------------------------------------- | ------------ |
| PDF        | `.pdf`                                                    | 支持文本型和扫描型    |
| 图片         | `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.bmp`, `.tiff` | 自动转换为 PDF 处理 |
| Word       | `.docx`                                                   | Office 文档    |
| PowerPoint | `.pptx`                                                   | 演示文稿         |
| Excel      | `.xlsx`                                                   | 电子表格         |

***

## 六、输出格式

### 6.1 文件输出

解析完成后，输出目录结构如下：

```
output/
└── document_name/
    └── vlm/                    # 或 pipeline/hybrid_auto/
        ├── document_name.md    # Markdown 结果
        ├── document_name_middle.json    # 中间数据
        ├── document_name_model.json     # 模型输出
        ├── document_name_content_list.json  # 内容列表
        ├── document_name_origin.pdf     # 原始文件
        └── images/             # 提取的图片
            ├── img_0.png
            └── img_1.png
```

### 6.2 API 响应格式

**成功响应（200 OK）：**

```json
{
  "task_id": "string",
  "status": "completed",
  "file_names": ["string"],
  "result": {
    "md": "string",
    "middle_json": "object",
    "content_list": "object"
  }
}
```

**失败响应（409 Conflict）：**

```json
{
  "task_id": "string",
  "status": "failed",
  "message": "string"
}
```

***

## 七、环境变量

| 变量名                              | 说明        | 默认值       |
| -------------------------------- | --------- | --------- |
| `MINERU_LOG_LEVEL`               | 日志级别      | INFO      |
| `MINERU_API_OUTPUT_ROOT`         | API 输出根目录 | ./output  |
| `MINERU_MAX_CONCURRENT_REQUESTS` | 最大并发请求数   | 4         |
| `MINERU_API_HOST`                | API 服务地址  | 127.0.0.1 |
| `MINERU_API_PORT`                | API 服务端口  | 8000      |

***

## 八、依赖安装

### 8.1 基础安装

```bash
pip install mineru
```

### 8.2 全功能安装

```bash
pip install mineru[core]
```

### 8.3 特定后端

```bash
# Pipeline 后端
pip install mineru[pipeline]

# VLM 后端
pip install mineru[vlm]

# MCP 支持
pip install mineru[mcp]
```

***

## 九、错误码说明

| 状态码 | 说明        |
| --- | --------- |
| 200 | 成功        |
| 202 | 任务已接受（异步） |
| 404 | 任务不存在     |
| 409 | 任务执行失败    |
| 503 | 服务不可用     |

