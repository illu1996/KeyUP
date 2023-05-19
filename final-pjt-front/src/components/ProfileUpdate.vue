<template>
  <div>
    <form @submit.prevent="updateUserProfile">
      <label for="nickname">닉네임</label>
      <input type="text" id="nickname" v-model="nickname">
      <label for="introduce">소개말</label>
      <input type="text" id="introduce" v-model="introduce">
      <input type="file" @change="FileUpload">
      <button>수정하기</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name :'ProfileUpdate',
  props:{
    user:Object
  },
  data() {
    return {
      nickname : null,
      introduce : null,
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
        url: `${API_URL}/accounts/about/${this.user.id}/updateprofile/`,
        headers : {
          "Authorization" : `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data'
        },
        data:{
          nickname, introduce,
          image: this.selectedFile
        }
      })
      .then((res)=>{
        console.log(res.data)
        this.$router.push('/profile/detail')
      })
    },
    FileUpload(event) {
      this.selectedFile = event.target.files[0];
    }
  }
}
</script>

<style>

</style>