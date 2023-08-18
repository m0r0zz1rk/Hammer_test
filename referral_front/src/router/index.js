import { createRouter, createWebHistory } from 'vue-router'
import store from '../store/index.js'

import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'
import Main from '../views/Main.vue'

const ifAuthenticated = (to, from, next) => {
  if (!(store.getters.isAuthenticated)) {
    showMessage('error', 'Пожалуйста, войдите в систему', false)
    next('/?nextUrl='+to.path)
    return
  } else {
    fetch(store.state.backendUrl+'/api/v1/auth/check_auth/', {
      method: 'GET',
      headers: {
          'Authorization': 'Token '+getCookie('access_token'),
      },
    })
    .then(resp => {
      if (resp.status == 401 || resp.status == 403) {
        showMessage('error', 'Пожалуйста, ввойдите в систему', false)
        next('/?nextUrl='+to.path)
        return
      } else if (resp.status == 500) {
        showMessage('error', 'Произошла внутренняя ошибка сервера', false)
        next('/?nextUrl='+to.path)
        return
      } else {
        next()
        return
      }
    })
  }
}

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/main',
    name: 'Main',
    component: Main,
    beforeEnter: ifAuthenticated
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    beforeEnter: ifAuthenticated
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
