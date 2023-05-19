<template>
  <div class="body container d-flex">
    <div class="loginform">
    <h2>로그인</h2>
    <form @submit.prevent="login">
      <label for="username">ID </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password">PASSWORD </label>
      <input type="password" id="password" v-model="password"><br>

      <button>LOGIN</button>
    </form>
    </div>
  </div>
</template>

<script>
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
.loginform {
box-sizing: border-box;
background: #FFFFFF;
border: 1px solid #FFFFFF;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

</style>