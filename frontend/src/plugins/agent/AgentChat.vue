<template>
  <section class="agent-chat">
    <h2>Agent 对话</h2>
    <form @submit.prevent="onSubmit">
      <textarea v-model="prompt" placeholder="请输入问题" required></textarea>
      <button type="submit">发送</button>
    </form>
    <article v-if="response" class="response">
      <h3>响应</h3>
      <p>{{ response.answer }}</p>
      <small>Engine: {{ response.engine }}</small>
    </article>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { http } from '@/core'

const prompt = ref('请介绍框架中的插件机制')
const response = ref(null)

const onSubmit = async () => {
  const { data } = await http.post('/agent/ask', { prompt: prompt.value })
  response.value = data
}
</script>

<style scoped>
.agent-chat {
  max-width: 600px;
}

textarea {
  width: 100%;
  min-height: 120px;
  margin-bottom: 1rem;
}

.response {
  margin-top: 2rem;
  padding: 1rem;
  background: #f5f5f5;
}
</style>
