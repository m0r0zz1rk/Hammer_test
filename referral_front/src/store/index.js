import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'

export default createStore({
  plugins: [createPersistedState({
    storage: window.localStorage,
  })],
  state: {
    backendUrl: process.env.VUE_APP_BACKEND_URL,
    token: getCookie('access_token') || '',
    status: ''
  },
  getters: {
    getServerUrl: state => state.backendUrl,
    isAuthenticated: state => !!state.token,
    authStatus: state => state.status,
  },
  mutations: {
    AUTH_REQUEST (state) {
        state.status = 'loading'
    },
    AUTH_SUCCESS (state, token) {
        state.status = 'success',
        state.token = token
    },
    AUTH_ERROR (state) {
        state.status = 'error'
    },
  },
  actions: {
    AUTH_REQUEST ({commit, dispatch}, user ) {
        return new Promise((resolve, reject) => { // The Promise used for router redirect in login
          commit('AUTH_REQUEST');
          fetch(this.state.backendUrl+'/api/v1/auth/login/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
            },
            body: JSON.stringify({
                'phone': user.phone,
                'auth_code': user.auth_code
            })
          })
          .then(resp => resp.json())
          .then(data => {
              if ('error' in data){
                commit('AUTH_ERROR', data.error)
                showMessage('error', data.error, false)
              } else {
                const token = data.success.token
                commit('AUTH_SUCCESS', token)
                setCookie('access_token', token)
                showMessage('success', 'Вход выполнен успешно', false);
                resolve();
              }
            })
          .catch(err => {
            commit('AUTH_ERROR', err)
            delCookie('access_token') // if the request fails, remove any possible user token if possible
            reject(err)
            showMessage('error', 'Неудачная попытка входа в систему. Поробуйте еще раз', false)
          })
          })
    },
    AUTH_LOGOUT ({commit, dispatch}) {
        return new Promise((resolve, reject) => {
          delCookie('access_token') // clear your user's token from localstorage
          resolve()
        })
    }
  },
  modules: {
  }
})