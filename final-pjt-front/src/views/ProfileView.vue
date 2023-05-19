<template>
  <div>
    ProfileView
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  methods:{
    getUserProfile() {
      axios({
        method : 'get',
        url: `${API_URL}/accounts/user/`,
        headers : {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        console.log(res.data)
      })
    }
  }
}
</script>

<style>

</style>