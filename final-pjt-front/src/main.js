import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLogin;

  if (!isLoggedIn) {
    if (to.name !== 'Login' && to.path !== '/signup')  {
      next({ name: 'Login' }); 
    } else {
      next()
    }
  } else {
    next()
  }
});

axios.interceptors.response.use(
  response => response,
  error => {
    // 현재 URL을 확인
    const currentURL = window.location.href;

    // 현재 URL이 로그인 화면의 경로 패턴과 일치하는지 확인
    if (currentURL.includes('/login')) {
      if (error.response.status === 404) {
        alert('아이디 혹은 비밀번호가 잘못되었습니다.');
        window.location.reload();
      }
    }
    
    return Promise.reject(error);
  }
);

new Vue({

  router,
  store,
  render: h => h(App)
}).$mount('#app')
