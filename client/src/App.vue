<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app-shell">
    <header class="top-bar">
      <RouterLink class="brand" to="/">Jetpack</RouterLink>
      <nav>
        <RouterLink to="/">项目状态</RouterLink>
      </nav>
    </header>

    <RouterView />
  </div>
</template>

<style scoped>
.app-shell {
  min-height: 100vh;
}

.top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  min-height: 64px;
  padding: 0 32px;
  border-bottom: 1px solid var(--color-border);
  background: var(--color-surface);
}

.brand {
  color: var(--color-heading);
  font-size: 20px;
  font-weight: 800;
  text-decoration: none;
}

nav {
  display: flex;
  align-items: center;
  gap: 16px;
}

nav a {
  color: var(--color-muted);
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: var(--color-heading);
}

@media (max-width: 720px) {
  .top-bar {
    padding: 0 20px;
  }
}
</style>
