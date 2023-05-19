<template>
  <div>
    <h3>마이페이지</h3>
    <router-link to="/profile/detail">상세페이지</router-link> |
    <router-link to="/profile/update">마이페이지 정보 수정</router-link> |
    <router-view :user="user"/>
    <!-- <ProfileDetail :user="user"/>
    <ProfileUpdate :user="user"/> -->
  </div>
</template>

<script>
import axios from 'axios';
// import ProfileDetail from '@/components/ProfileDetail.vue'
// import ProfileUpdate from '@/components/ProfileUpdate.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  // components: {
  //   ProfileDetail,
  //   ProfileUpdate
  // },
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
        console.log(res.data)
        this.user = res.data
      })
    },
  },
  created() {
    this.getUserProfile()
  }
}
</script>

<style>

</style>