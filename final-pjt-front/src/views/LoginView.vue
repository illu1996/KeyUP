<template>
  <div>
    <div>
      <video class="bg-video" playsinline="playsinline" autoplay="autoplay" muted="muted" loop="loop">
        <source src="@/assets/bg.mp4" type="video/mp4" />
      </video>
      <div>
      <div class="overlay"></div>
      <div class="loginform">
        <h2>로그인</h2>
        <form @submit.prevent="login">
          <label for="username">ID </label>
          <input type="text" id="username" v-model="username"><br>
  
          <label for="password">PASSWORD </label>
          <input type="password" id="password" v-model="password"><br>
  
          <button>LOGIN</button>
        </form>
        <router-link :to="{ name: 'Signup' }">회원가입</router-link>
      </div>
    </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },

  methods: {
    login() {
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    }
  }
}
</script>


<style>
.video-container {
  position: relative;
}

video.bg-video {
  position: fixed;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  transform: translateX(-50%) translateY(-50%);
  z-index: -1;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 60%;
  height: 100%;
  background-color: black;
  opacity: 0.8;
  z-index: 1;
}

.loginform {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}
</style>