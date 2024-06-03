import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import '@/assets/font_4508119_m6yo9pspueh/iconfont.css'
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
