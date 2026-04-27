# Jetpack Server

FastAPI 后端服务。

## 环境

- Python 3.13+
- uv

## 安装

```bash
uv sync
```

## 启动

```bash
uv run fastapi dev src/jetpack_api/main.py
```

Windows 后台或控制台编码异常时可使用：

```bash
uv run uvicorn jetpack_api.main:app --reload --app-dir src
```

## 测试

```bash
uv run pytest
```

## 目录

```text
openapi/          OpenAPI 接口契约
src/jetpack_api/  后端应用代码
tests/            后端测试
```
