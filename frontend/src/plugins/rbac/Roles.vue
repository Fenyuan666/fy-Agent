<template>
  <section class="roles">
    <h2>角色列表</h2>
    <button @click="seed">初始化示例角色</button>
    <ul>
      <li v-for="role in roles" :key="role.name">
        <strong>{{ role.name }}</strong>
        <span v-if="role.permissions.length"> - {{ role.permissions.map((p) => p.code).join(', ') }}</span>
      </li>
    </ul>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { http } from '@/core'

const roles = ref([])

const fetchRoles = async () => {
  const { data } = await http.get('/rbac/roles')
  roles.value = data
}

const seed = async () => {
  await http.post('/rbac/roles', {
    name: 'admin',
    permissions: [
      { code: 'agent:read' },
      { code: 'agent:write' },
    ],
  })
  fetchRoles()
}

onMounted(fetchRoles)
</script>

<style scoped>
.roles {
  max-width: 480px;
}
</style>
