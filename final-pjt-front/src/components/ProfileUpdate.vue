<template>
  <div id="modal">
    <form @submit.prevent="updateUserProfile">
      <div class="input-wrapper">
        <div class="label-wrapper">
          <label for="nickname">닉네임</label>
        </div>
        <input
          type="text"
          id="nickname"
          v-model="nickname"
          required
        >
      </div>
      <br>
      <div class="input-wrapper">
        <div class="label-wrapper">
          <label for="introduce">소개말</label>
        </div>
        <input
          type="text"
          id="introduce"
          v-model="introduce"
          required
        >
      </div>
      <div class="file-input-container">

          <span>{{ selectedFileName }}</span>
          <input type="file" id="file-input" class="file-input" @change="onFileChange">
          <label for="file-input" class="file-input-label"></label>

      </div>
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
      nickname : this.$store.state.nickname,
      introduce : this.$store.state.introduce,
      selectedFile : null,
      selectedFileName: '',
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
        this.$router.push(`/profile/detail/${this.$store.state.username}`).catch(()=>{})
        this.disappear()
        const payload = {
          nickname : res.data.nickname,
          introduce : res.data.introduce,
          profileimg : res.data.profileimg

        }
        this.$store.dispatch('changeInfo', payload)
      })
    },
    changeProfile(info) {
      const userInfo = info
      this.$store.dispatch('changeProfile', userInfo)
    },
    onFileChange(event) {
      console.log(event.target.files[0].name)
      this.selectedFile = event.target.files[0];
      if (event.target.files[0].name.length > 13) {
        this.selectedFileName = event.target.files[0].name.slice(0, 13) + '...'
      } else {
        this.selectedFileName = event.target.files[0].name
      }
    },
    disappear() {
      this.$emit('disappearComp')
    }
  }
}
</script>

<style scoped>
#modal {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

form {
  text-align: center;
}

label {
  display: inline-block;
  margin-bottom: 0px;
  font-weight: bold;
  text-align: left;
}

input[type="text"] {
  display: block;
  width: 100%;
  padding: 5px;
  font-size: 16px;
  border: none;
  border-bottom: 2px solid #ccc;
  border-radius: 0;
  margin-bottom: 0px;
  outline: none;
}

.file-input-container {
  position: relative;
  display: inline-block;
  margin-bottom: 0px;
}

.label-wrapper {
  display: flex;
  align-items: center;
}

.label-wrapper label {
  margin-right: 10px;
}

.input-wrapper {
  margin-bottom: 10px;
}

.file-input {
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}

.file-input-label {
  display: inline-block;
  padding: 5px;
  color: #000;
  border: 2px solid #ccc;
  cursor: pointer;
}

button {
  display: block;
  padding: 5px 10px;
  font-size: 16px;
  background-color: #090a11;
  color: #fff;
  border: none;
  cursor: pointer;
  margin-left: auto;
}


.file-input-container {
  position: relative;
  display: inline-block;
  margin-bottom: 10px;
}

.file-input {
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}

.file-input-label {
  display: inline-block;
  padding: 5px;
  color: #000;
  border: 2px solid #ccc;
  cursor: pointer;
}

.file-input-label::after {
  content: '파일 선택';
}

.file-input-label:hover {
  background-color: #ddf;
}

.file-input-label:active {
  background-color: #ccd;
}

.file-input-label:focus {
  outline: none;
  box-shadow: 0 0 0 2px #99c;
}
</style>
