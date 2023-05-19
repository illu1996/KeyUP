<template>
  <div>
    <form @submit.prevent="updateUserProfile">
      <label for="nickname">닉네임</label>
      <input type="text" id="nickname" v-model="nickname">
      <label for="introduce">소개말</label>
      <input type="text" id="introduce" v-model="introduce">
      <input type="file" @change="onFileChange">
      <button>수정하기</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name :'ProfileUpdate',
  data() {
    return {
      nickname : null,
      introduce : null,
      selectedFile : null,
    }
  },
  methods: {
    updateUserProfile() {
      const nickname = this.nickname
      const introduce = this.introduce
      const formData = new FormData();
      formData.append('image', this.selectedFile);

      axios({
        method : 'post',
        url: `${API_URL}/accounts/about/${this.$store.state.userInfo.id}/updateprofile/`,
        headers : {
          "Authorization" : `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data'
        },
        data:{
          nickname, introduce,
          profileimg: this.selectedFile
        }
      })
      .then((res)=>{
        this.changeProfile(res.data)
        this.$router.push('/profile/detail')
      })
    },
    changeProfile(info) {
      const userInfo = info
      this.$store.dispatch('changeProfile', userInfo)
    },
    onFileChange(event) {
      console.log(event.target.files[0])
      this.selectedFile = event.target.files[0];
    },
  }
}
</script>

<style>

</style>