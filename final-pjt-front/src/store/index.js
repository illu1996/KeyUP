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
    profileimg : null,
    nickname : null,
    introduce : null,
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
      state.profileimg = null
      state.nickname = null
      state.introduce = null
    },
    CHANGE_INFO(state, payload) {
      state.profileimg = payload.profileimg
      state.nickname = payload.nickname
      state.introduce = payload.introduce
    },
  },
  actions: {
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      const profileimg = payload.pimg
      const nickname = payload.nickname
      const introduce = payload.introduce
      
      axios({
        method : 'post',
        url : `${API_URL}/accounts/login/`,
        data : {
          username, password, profileimg, nickname, introduce
        }
      })
      .then((res)=>{

        this.state.username = username
        this.state.profileimg = profileimg
        this.state.nickname = nickname
        this.state.introduce = introduce
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
        this.state.username = username
        this.state.profileimg = null
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(()=>{
        if (username === password1) {
          alert ('아이디는 비밀번호로 사용하실 수 없습니다.')
        }
        else if (password1!==password2) {
          alert ('비밀번호와 비밀번호 확인이 다릅니다.')
        }
        else {
          alert ('사용할 수 없는 아이디 입니다.')
        }
      })
    },
    changeMovie(context, payload) {
      context.commit('CHANGE_MOVIE', payload)
    },
    changeProfile(context, payload) {
      context.commit('CHANGE_PROFILE', payload)
    },
    changeInfo(context, payload) {
      context.commit('CHANGE_INFO', payload)
    },
  },
  modules: {
  }
})
