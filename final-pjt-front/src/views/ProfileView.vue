<template>
  <div>
    <h3>회원정보</h3>
    <div v-if="this.$route.params.username === this.$store.state.username">
    <router-link to="/profile/update">마이페이지 정보 수정</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      user : null,
    }
  },
  methods:{
    getUserProfile() {
      axios({
        method : 'get',
        url: `${API_URL}/accounts/about/${this.$store.state.username}/profile/`,
        headers : {
          "Authorization" : `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        this.user = res.data
        this.changeProfile()
      })
    },
    changeProfile() {
      const userInfo = this.user
      this.$store.dispatch('changeProfile', userInfo)
    }
  },
  created() {
    this.getUserProfile()
  }
}
</script>

<style>

</style>