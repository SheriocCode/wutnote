import axios from 'axios'

// 创建axios实例
const httpInstance = axios.create({
  // baseURL: 'https://mock.apifox.cn/m1/4248529-3889906-default',
  baseURL:'http://127.0.0.1:8000',
  timeout: 5000
})

// // axios请求拦截器
// instance.interceptors.request.use(config => {
//   return config
// }, e => Promise.reject(e))

// // axios响应式拦截器
// instance.interceptors.response.use(res => res.data, e => {
//   return Promise.reject(e)
// })


export default httpInstance