# MinerU REST API 接口文档

## 概述

MinerU 是一个强大的文档解析工具，支持将 PDF、图片、Office 文档转换为 Markdown/JSON 格式。本文档详细描述其 REST API 接口。

---

## 一、服务启动

```bash
mineru-api [--host HOST] [--port PORT]
```

**默认地址**：`http://127.0.0.1:8000`

**API 文档访问**：
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 二、API 端点列表

| HTTP 方法 | 端点路径 | 功能描述 |
|-----------|---------|---------|
| **POST** | `/file_parse` | 同步解析文件（等待完成后返回结果） |
| **POST** | `/tasks` | 异步提交解析任务（立即返回任务ID） |
| **GET** | `/tasks/{task_id}` | 查询任务状态 |
| **GET** | `/tasks/{task_id}/result` | 获取任务结果 |
| **GET** | `/health` | 健康检查 |

---

## 三、接口详细说明

### 3.1 POST /file_parse（同步文件解析）

**功能**：上传文件并同步等待解析完成，直接返回结果。

**支持的文件类型**：PDF、图片（png/jpg/webp/gif/bmp/tiff）、DOCX、PPTX、XLSX

**请求参数**（Multipart Form Data）：

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `files` | File | ✅ | - | 上传的文件（支持多文件） |
| `backend` | str | ❌ | hybrid-auto-engine | 解析后端引擎 |
| `parse_method` | str | ❌ | auto | 解析方法：auto/txt/ocr |
| `lang_list` | list[str] | ❌ | ["ch"] | 语言代码列表 |
| `formula_enable` | bool | ❌ | true | 启用公式解析 |
| `table_enable` | bool | ❌ | true | 启用表格解析 |
| `image_analysis` | bool | ❌ | true | 启用图片/图表分析 |
| `server_url` | str | ❌ | null | openai兼容服务器地址（用于http-client后端） |
| `return_md` | bool | ❌ | true | 返回 Markdown 内容 |
| `return_middle_json` | bool | ❌ | false | 返回中间 JSON |
| `return_model_output` | bool | ❌ | false | 返回模型输出 JSON |
| `return_content_list` | bool | ❌ | false | 返回内容列表 JSON |
| `return_images` | bool | ❌ | false | 返回提取的图片（Base64） |
| `response_format_zip` | bool | ❌ | false | ZIP 格式返回 |
| `return_original_file` | bool | ❌ | false | 包含原始文件（仅 ZIP 模式有效） |
| `start_page_id` | int | ❌ | 0 | 起始页码（从0开始） |
| `end_page_id` | int | ❌ | 99999 | 结束页码 |

**请求示例**：
```bash
curl -X POST http://127.0.0.1:8000/file_parse \
  -F "files=@document.pdf" \
  -F "backend=pipeline" \
  -F "lang_list=ch" \
  -F "return_md=true"
```

**成功响应**（200 OK）：
```json
{
  "task_id": "uuid-string",
  "status": "completed",
  "backend": "pipeline",
  "version": "2.5.0",
  "results": {
    "document": {
      "md_content": "# 文档标题\n\n正文内容..."
    }
  }
}
```

**失败响应**（409 Conflict）：
```json
{
  "task_id": "uuid-string",
  "status": "failed",
  "error": "解析失败原因",
  "message": "Task execution failed"
}
```

---

### 3.2 POST /tasks（异步任务提交）

**功能**：提交文件解析任务，立即返回任务信息，不等待完成。

**请求参数**：与 `/file_parse` 相同

**请求示例**：
```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -F "files=@document.pdf" \
  -F "backend=hybrid-auto-engine"
```

**响应**（202 Accepted）：
```json
{
  "task_id": "uuid-string",
  "status": "pending",
  "file_names": ["document"],
  "created_at": "2024-01-01T12:00:00Z",
  "status_url": "http://127.0.0.1:8000/tasks/uuid-string",
  "result_url": "http://127.0.0.1:8000/tasks/uuid-string/result",
  "message": "Task submitted successfully"
}
```

---

### 3.3 GET /tasks/{task_id}（查询任务状态）

**功能**：查询指定任务的当前状态。

**路径参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `task_id` | str | 任务唯一标识符 |

**请求示例**：
```bash
curl http://127.0.0.1:8000/tasks/uuid-string
```

**响应**：
```json
{
  "task_id": "uuid-string",
  "status": "processing",
  "file_names": ["document"],
  "created_at": "2024-01-01T12:00:00Z",
  "started_at": "2024-01-01T12:00:01Z",
  "completed_at": null,
  "queued_ahead": 0,
  "status_url": "http://127.0.0.1:8000/tasks/uuid-string",
  "result_url": "http://127.0.0.1:8000/tasks/uuid-string/result"
}
```

**状态说明**：

| 状态 | 说明 |
|------|------|
| `pending` | 等待处理 |
| `processing` | 处理中 |
| `completed` | 完成 |
| `failed` | 失败 |

---

### 3.4 GET /tasks/{task_id}/result（获取任务结果）

**功能**：获取已完成任务的解析结果。

**路径参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `task_id` | str | 任务唯一标识符 |

**请求示例**：
```bash
curl http://127.0.0.1:8000/tasks/uuid-string/result
```

**响应**（200 OK - JSON 格式）：
```json
{
  "task_id": "uuid-string",
  "status": "completed",
  "backend": "pipeline",
  "version": "2.5.0",
  "results": {
    "document": {
      "md_content": "# 文档标题\n\n正文内容..."
    }
  }
}
```

**响应**（202 Accepted - 任务未完成）：
```json
{
  "task_id": "uuid-string",
  "status": "processing",
  "message": "Task result is not ready yet"
}
```

**响应**（409 Conflict - 任务失败）：
```json
{
  "task_id": "uuid-string",
  "status": "failed",
  "error": "失败原因",
  "message": "Task execution failed"
}
```

---

### 3.5 GET /health（健康检查）

**功能**：检查 API 服务状态和任务队列情况。

**请求示例**：
```bash
curl http://127.0.0.1:8000/health
```

**响应**（200 OK - 健康）：
```json
{
  "status": "healthy",
  "version": "2.5.0",
  "protocol_version": 1,
  "queued_tasks": 0,
  "processing_tasks": 1,
  "completed_tasks": 10,
  "failed_tasks": 0,
  "max_concurrent_requests": 4,
  "processing_window_size": 64,
  "task_retention_seconds": 86400,
  "task_cleanup_interval_seconds": 300
}
```

**响应**（503 Service Unavailable - 不健康）：
```json
{
  "status": "unhealthy",
  "version": "2.5.0",
  "error": "Task manager is not initialized"
}
```

---

## 四、支持的后端引擎

| 后端引擎 | 说明 | 依赖要求 |
|---------|------|---------|
| `pipeline` | 通用解析模式，支持多语言 | 需要 `mineru[pipeline]` |
| `vlm-auto-engine` | 本地 VLM 高精度模式 | 需要 `mineru[vlm]` |
| `vlm-http-client` | 远程 VLM 客户端 | 无需本地 torch |
| `hybrid-auto-engine` | 本地混合高精度模式（推荐） | 需要 `mineru[core]` |
| `hybrid-http-client` | 远程混合客户端 | 需要 `mineru[pipeline]` |

---

## 五、支持的语言代码

| 代码 | 语言 |
|------|------|
| `ch` | 中文、英文、繁体中文 |
| `ch_lite` | 中文、英文、繁体中文、日语 |
| `ch_server` | 中文、英文、繁体中文、日语 |
| `en` | 英文 |
| `korean` | 韩语、英文 |
| `japan` | 中文、英文、繁体中文、日语 |
| `chinese_cht` | 中文、英文、繁体中文、日语 |
| `ta` | 泰米尔语、英文 |
| `te` | 泰卢固语、英文 |
| `ka` | 卡纳达语 |
| `th` | 泰语、英文 |
| `el` | 希腊语、英文 |
| `latin` | 法语、德语、西班牙语等多种拉丁语系语言 |
| `arabic` | 阿拉伯语、波斯语、乌尔都语等 |
| `east_slavic` | 俄语、白俄罗斯语、乌克兰语 |
| `cyrillic` | 俄语、保加利亚语、蒙古语等 |
| `devanagari` | 印地语、马拉地语、尼泊尔语等 |

---

## 六、输出格式说明

### 6.1 返回字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `md_content` | string | Markdown 格式的文档内容 |
| `middle_json` | string | 中间表示层 JSON |
| `model_output` | string | 模型原始输出 JSON |
| `content_list` | string | 内容列表格式 JSON |
| `images` | object | Base64 编码的图片字典 |

### 6.2 ZIP 输出模式

当 `response_format_zip=true` 时，返回一个 ZIP 文件，包含：
- `<filename>.md` - Markdown 文件
- `<filename>_middle.json` - 中间 JSON
- `<filename>_model.json` - 模型输出
- `<filename>_content_list.json` - 内容列表
- `images/` - 提取的图片目录

---

## 七、错误码说明

| 状态码 | 说明 |
|--------|------|
| **200** | 请求成功 |
| **202** | 任务已接受（异步任务） |
| **400** | 请求参数错误 |
| **404** | 任务不存在 |
| **409** | 任务执行失败 |
| **503** | 服务不可用 |

---

## 八、环境变量配置

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `MINERU_API_HOST` | API 服务绑定地址 | 127.0.0.1 |
| `MINERU_API_PORT` | API 服务端口 | 8000 |
| `MINERU_API_OUTPUT_ROOT` | 输出目录 | ./output |
| `MINERU_MAX_CONCURRENT_REQUESTS` | 最大并发请求数 | 4 |
| `MINERU_API_TASK_RETENTION_SECONDS` | 任务保留时间（秒） | 86400 |
| `MINERU_API_TASK_CLEANUP_INTERVAL_SECONDS` | 任务清理间隔（秒） | 300 |
| `MINERU_API_ENABLE_FASTAPI_DOCS` | 是否启用 API 文档 | true |

---

## 九、代码参考

API 实现在以下文件中：

| 文件 | 说明 |
|------|------|
| [fast_api.py](file:///home/tlw/PycharmProjects/mcp/MinerU/mineru/cli/fast_api.py) | FastAPI 服务实现 |
| [api_protocol.py](file:///home/tlw/PycharmProjects/mcp/MinerU/mineru/cli/api_protocol.py) | API 协议定义 |
| [mineruApi.js](file:///home/tlw/PycharmProjects/mcp/MinerU/frontend/src/services/mineruApi.js) | 前端 API 封装 |

---

## 十、使用示例

### 示例 1：同步解析 PDF
```bash
curl -X POST http://127.0.0.1:8000/file_parse \
  -F "files=@document.pdf" \
  -F "backend=pipeline" \
  -F "lang_list=ch" \
  -F "return_md=true"
```

### 示例 2：异步提交任务并轮询结果
```bash
# 提交任务
RESPONSE=$(curl -X POST http://127.0.0.1:8000/tasks \
  -F "files=@document.pdf" \
  -F "backend=hybrid-auto-engine")

TASK_ID=$(echo $RESPONSE | jq -r '.task_id')

# 轮询状态
while true; do
  STATUS=$(curl -s http://127.0.0.1:8000/tasks/$TASK_ID | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ] || [ "$STATUS" = "failed" ]; then
    break
  fi
  sleep 2
done

# 获取结果
curl http://127.0.0.1:8000/tasks/$TASK_ID/result
```

### 示例 3：获取 ZIP 格式结果
```bash
curl -X POST http://127.0.0.1:8000/file_parse \
  -F "files=@document.pdf" \
  -F "backend=pipeline" \
  -F "return_md=true" \
  -F "return_images=true" \
  -F "response_format_zip=true" \
  -o result.zip
```
