import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect:'/user'
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
        component: () => import('@/views/index/index.vue'),
        meta: { requiresAuth: false }
      },{
        path: '/create',
        name: 'create',
        component: () => import('@/views/create/create.vue'),
        meta: { requiresAuth: true }
      },{
        path: '/user',
        name: 'user',
        component: () => import('@/views/user/user.vue'),
        // meta: { requiresAuth: true }
      },{
        path: '/my',
        name: 'my',
        component: () => import('@/views/my/my.vue'),
        meta: { requiresAuth: true }
      }]
    },{
      path: '/note/:id',
      name: 'note',
      component: () => import('@/views/noteDetails/noteDetails.vue'),
      meta: { requiresAuth: false }
    }
  ]
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth) {
    if (token) {
      next();
    } else {
      next('/login');
    }
  } else {
    next();
  }
})


export default router
