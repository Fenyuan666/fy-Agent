import axios from 'axios'

const http = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || '/api/v1',
})

http.interceptors.request.use((config) => {
  const injectedEmail = import.meta.env.VITE_MOCK_USER_EMAIL
  if (injectedEmail) {
    config.headers['X-User-Email'] = injectedEmail
  }
  return config
})

export default http
