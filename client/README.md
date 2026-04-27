# Jetpack Client

Vue 3 客户端工程，用于 Jetpack 横板跳跃闯关游戏的网页登录、游戏入口、商店等界面。

当前阶段只提供可启动的项目骨架，不实现游戏玩法。

## 环境

- Node.js 20.19+ 或 22.12+
- npm

## 安装

```bash
npm install
```

## 启动

```bash
npm run dev
```

## 检查

```bash
npm run lint
npm run type-check
npm run test:unit
npm run build
```

## 接口配置

复制 `.env.example` 为 `.env.local` 后可调整后端地址：

```text
VITE_API_BASE_URL=http://localhost:8000
```

