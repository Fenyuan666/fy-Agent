import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', component: () => import('./components/HomeView.vue') },
]

if (import.meta.env.VITE_FEATURE_AGENT === 'true') {
  routes.push({ path: '/agent', component: () => import('../plugins/agent/AgentChat.vue') })
}

if (import.meta.env.VITE_FEATURE_AUTH === 'true') {
  routes.push({ path: '/login', component: () => import('../plugins/auth/Login.vue') })
}

if (import.meta.env.VITE_FEATURE_RBAC === 'true') {
  routes.push({ path: '/roles', component: () => import('../plugins/rbac/Roles.vue') })
}

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
