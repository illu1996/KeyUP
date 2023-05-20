<template>
  <div id="app">
    <nav>
      <router-link to="/">Main</router-link> |
      <router-link to="/movies/all">Movie</router-link> |
      <router-link to="/recommend">Recommend</router-link> |
      <router-link to="/community">community</router-link> |

      <div v-if="!displayLogin">
        <router-link to="/signup">Sign-Up</router-link> |
        <router-link to="/login">Login</router-link> |
      </div>
      <div v-else>
        <router-link :to="`/profile/detail/${username}`">Profile</router-link> |
        <span @click="logout">로그아웃</span>
      </div>
      <div>
        <input type="text" v-model="search">
        <button @click="searchMovie">검색하기</button>
      </div>
    </nav>
    <router-view />
  </div>
</template>


<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'app',
  computed: {
    displayLogin() {
      return this.$store.getters.isLogin
    },
    username() {
      return this.$store.state.username
    }
  },
  data() {
    return {
      search: null,
    }
  },
  methods: {
    logout() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {

          this.$store.commit('REMOVE_TOKEN')
          this.$router.push({ name: 'Login' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    searchMovie() {
      this.$router.push({ path: '/search', query: { keyword: this.search } })
      this.search = null
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
