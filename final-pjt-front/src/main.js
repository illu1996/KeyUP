import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

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


new Vue({

  router,
  store,
  render: h => h(App)
}).$mount('#app')
