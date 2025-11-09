<template>
  <section class="home">
    <h1>fy-Agent Framework</h1>
    <p>前往侧边栏或顶部导航体验已启用的模块。</p>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const enabledModules = computed(() => {
  const modules = []
  if (import.meta.env.VITE_FEATURE_AGENT === 'true') modules.push('Agent')
  if (import.meta.env.VITE_FEATURE_AUTH === 'true') modules.push('Auth')
  if (import.meta.env.VITE_FEATURE_RBAC === 'true') modules.push('RBAC')
  return modules
})
</script>

<style scoped>
.home {
  padding: 3rem;
}

.home h1 {
  margin-bottom: 1rem;
}
</style>
