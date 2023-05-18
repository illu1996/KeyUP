<template>
  <div>
    <h2>로그인</h2>
    <form @submit.prevent="login">
      <label for="username">아이디 </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password">비밀번호 </label>
      <input type="password" id="password" v-model="password"><br>

      <button>로그인</button>
    </form>
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

</style>