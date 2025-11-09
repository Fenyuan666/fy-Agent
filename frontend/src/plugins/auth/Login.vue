<template>
  <form class="login-form" @submit.prevent="onSubmit">
    <h2>登录</h2>
    <label>
      邮箱
      <input v-model="form.email" type="email" required />
    </label>
    <label>
      密码
      <input v-model="form.password" type="password" required />
    </label>
    <button type="submit">登录</button>
    <p v-if="error" class="error">{{ error }}</p>
  </form>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { http } from '@/core'

const form = reactive({
  email: 'demo@example.com',
  password: 'password',
})

const error = ref('')

const onSubmit = async () => {
  error.value = ''
  try {
    await http.post('/auth/login', form)
    alert('登录成功（示例）')
  } catch (err) {
    error.value = err?.response?.data?.detail || '登录失败'
  }
}
</script>

<style scoped>
.login-form {
  max-width: 320px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.error {
  color: #f44336;
}
</style>
