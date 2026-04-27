<template>
  <main class="home">
    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow">Project Initialized</p>
        <h1>Jetpack</h1>
        <p class="summary">
          横板跳跃闯关网页游戏骨架已就绪。当前阶段包含客户端、后端、接口契约、文档规范和协作模板。
        </p>
      </div>

      <div class="status-panel">
        <div>
          <span class="label">Client</span>
          <strong>Vue 3 + Vite</strong>
        </div>
        <div>
          <span class="label">Server</span>
          <strong>FastAPI + uv</strong>
        </div>
        <div>
          <span class="label">Scope</span>
          <strong>Structure only</strong>
        </div>
      </div>
    </section>

    <section class="workflow">
      <h2>基础模块</h2>
      <div class="module-grid">
        <article>
          <h3>账号</h3>
          <p>预留注册、登录和鉴权模块。</p>
        </article>
        <article>
          <h3>关卡</h3>
          <p>预留横板闯关入口和玩法工程位置。</p>
        </article>
        <article>
          <h3>商店</h3>
          <p>预留人物皮肤购买和展示模块。</p>
        </article>
      </div>
    </section>
  </main>
</template>

<style scoped>
.home {
  min-height: calc(100vh - 64px);
  background:
    linear-gradient(180deg, rgba(246, 248, 252, 0.9), rgba(255, 255, 255, 0.96)),
    radial-gradient(circle at 80% 10%, rgba(255, 196, 87, 0.32), transparent 32%),
    radial-gradient(circle at 20% 20%, rgba(70, 137, 255, 0.22), transparent 28%);
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(280px, 0.8fr);
  gap: 32px;
  align-items: end;
  max-width: 1120px;
  margin: 0 auto;
  padding: 88px 32px 44px;
}

.eyebrow {
  margin: 0 0 12px;
  color: var(--color-accent);
  font-size: 13px;
  font-weight: 800;
  text-transform: uppercase;
}

h1 {
  margin: 0;
  color: var(--color-heading);
  font-size: clamp(48px, 8vw, 96px);
  font-weight: 900;
  line-height: 0.95;
}

.summary {
  max-width: 680px;
  margin: 24px 0 0;
  color: var(--color-text);
  font-size: 18px;
}

.status-panel {
  display: grid;
  gap: 16px;
  padding: 24px;
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background: var(--color-surface);
  box-shadow: 0 18px 48px rgba(24, 35, 56, 0.12);
}

.status-panel div {
  display: grid;
  gap: 4px;
}

.label {
  color: var(--color-muted);
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
}

.status-panel strong {
  color: var(--color-heading);
  font-size: 18px;
}

.workflow {
  max-width: 1120px;
  margin: 0 auto;
  padding: 32px 32px 72px;
}

h2 {
  margin: 0 0 18px;
  color: var(--color-heading);
  font-size: 24px;
  font-weight: 850;
}

.module-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

article {
  min-height: 132px;
  padding: 22px;
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.84);
}

h3 {
  margin: 0 0 10px;
  color: var(--color-heading);
  font-size: 18px;
  font-weight: 800;
}

article p {
  margin: 0;
  color: var(--color-muted);
}

@media (max-width: 820px) {
  .hero,
  .module-grid {
    grid-template-columns: 1fr;
  }

  .hero {
    padding: 56px 20px 28px;
  }

  .workflow {
    padding: 24px 20px 56px;
  }
}
</style>
