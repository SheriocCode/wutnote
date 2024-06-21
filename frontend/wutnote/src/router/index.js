import { createRouter, createWebHistory } from 'vue-router'
// import { useUserStore } from '@/stores/user'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect:'/create'
    },{
      path: '/login',
      name: 'login',
      component: () => import('@/views/login/login.vue')
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
      },{
        path: '/create',
        name: 'create',
        component: () => import('@/views/create/create.vue')
      },{
        path: '/my',
        name: 'my',
        component: () => import('@/views/my/my.vue')
      }]
    }
  ]
})

// const user = useUserStore()
// router.beforeEach((to, from, next) => {
//   if (to.path === '/my' && !user.token) {
//     next('/login');
//   } else {
//     next();
//   }
// }
// )
export default router
