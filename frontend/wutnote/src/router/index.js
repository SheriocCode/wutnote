import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect:'/create'
    },{
      path: '/',
      name: 'index',
      component: () => import('@/views/layout/layout.vue'),
      children:[{
        path: '/home',
        name: 'home',
        component: () => import('@/views/index/index.vue')
      },{
        path: '/note/:id',
        name: 'note',
        component: () => import('@/views/noteDetails/noteDetails.vue')
      }]
    },{
      path: '/create',
      name: 'create',
      component: () => import('@/views/create/create.vue')
    }
  ]
})

export default router
