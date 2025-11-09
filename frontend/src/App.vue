<template>
  <div class="app-shell">
    <header>
      <h1>fy-Agent 控制台</h1>
      <nav>
        <RouterLink to="/">首页</RouterLink>
        <RouterLink v-if="featureAgent" to="/agent">Agent</RouterLink>
        <RouterLink v-if="featureAuth" to="/login">登录</RouterLink>
        <RouterLink v-if="featureRbac" to="/roles">角色</RouterLink>
      </nav>
    </header>
    <main>
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const featureAgent = computed(() => import.meta.env.VITE_FEATURE_AGENT === 'true')
const featureAuth = computed(() => import.meta.env.VITE_FEATURE_AUTH === 'true')
const featureRbac = computed(() => import.meta.env.VITE_FEATURE_RBAC === 'true')
</script>

<style scoped>
.app-shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  background: #20232a;
  color: #fff;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav {
  display: flex;
  gap: 1rem;
}

main {
  flex: 1;
  padding: 2rem;
}

a {
  color: #61dafb;
  text-decoration: none;
}

a.router-link-active {
  font-weight: bold;
}
</style>
