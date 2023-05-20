import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedStated from 'vuex-persistedstate'
import router from '../router'
const API_URL = 'http://127.0.0.1:8000'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedStated(),
  ],
  state: {
    token : null,
    movie_info : null,
    username : null,
    userInfo : null,
    usersInfo : [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name:'Main'})
    },
    CHANGE_MOVIE(state, movieinfo) {
      state.movie_info = movieinfo
    },
    CHANGE_PROFILE(state, userInfo) {
      state.userInfo = userInfo;
    
      const index = state.usersInfo.findIndex((info) => info.id === userInfo.id);
    
      if (index !== -1) {
        state.usersInfo[index] = userInfo;
      } else {
        state.usersInfo.push(userInfo);
      }

    },
    REMOVE_TOKEN(state){
      state.token = null
      state.movie_info = null
      state.username = null
      state.userInfo = null
    },
  },
  actions: {
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      
      axios({
        method : 'post',
        url : `${API_URL}/accounts/login/`,
        data : {
          username, password
        }
      })
      .then((res)=>{
        console.log(res)
        this.state.username = username
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    signup(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method : 'post',
        url : `${API_URL}/accounts/signup/`,
        data : {
          username, password1, password2
        }
      })
      .then((res)=>{
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    changeMovie(context, payload) {
      context.commit('CHANGE_MOVIE', payload)
    },
    changeProfile(context, payload) {
      context.commit('CHANGE_PROFILE', payload)
    }
  },
  modules: {
  }
})
