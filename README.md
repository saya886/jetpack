# Jetpack

Jetpack 是一个横板跳跃闯关网页游戏项目。当前仓库已完成基础项目初始化，包含 Vue 客户端、FastAPI 后端、OpenAPI 契约、AI 协作入口、规范文档、Issue/PR 模板和美术资源目录。

本阶段只配置项目结构与可启动骨架，不实现实际游戏玩法。

## 技术栈

- 客户端：Vue 3、Vite、TypeScript、Pinia、Vue Router、Vitest
- 后端：Python、FastAPI、uv、pytest
- 接口契约：OpenAPI
- 协作流程：Issue -> Branch -> PR -> main

## 快速启动

客户端：

```bash
cd client
npm install
npm run dev
```

后端：

```bash
cd server
uv sync
uv run fastapi dev src/jetpack_api/main.py
```

Windows 后台或控制台编码异常时可使用：

```bash
cd server
uv run uvicorn jetpack_api.main:app --reload --app-dir src
```

默认地址：

- 客户端：`http://localhost:5173`
- 后端：`http://localhost:8000`
- 接口文档：`http://localhost:8000/docs`

## 目录说明

```text
.agents/        AI 可复用工作流
.github/        GitHub Issue 与 PR 模板
art/            美术资源交付目录
client/         Vue 客户端工程
docs/           项目规范和功能说明
ops/            运维和部署说明
server/         FastAPI 后端工程
```

## 必读文档

- [AI 入口索引](AGENTS.md)
- [总体工作流](docs/规范/总体工作流.md)
- [客户端规则](docs/规范/客户端规则.md)
- [后端规则](docs/规范/后端规则.md)
- [接口规则](docs/规范/接口规则.md)
- [项目概览](docs/功能/项目概览.md)
