<template>
  <div id="app">
    <header id="header" class="fixed-header">
      <div v-if="displayLogin">
        <nav id="navbar" class="navbar">
          <ul>
            <router-link class="nav-lin" to="/"><img id="logo" src="@/assets/logo.png" alt=""></router-link>
            <router-link class="nav-link" to="/">홈</router-link>
            <router-link class="nav-link" to="/movies">영화</router-link>
            <router-link class="nav-link" to="/recommend">나만을 위한 추천</router-link>
            <router-link class="nav-link" to="/community/list">커뮤니티</router-link>
          </ul>
          <ul>
            <div class='d-flex' v-if="!displayLogin">
              <router-link class="nav-link" to="/signup">Sign-Up</router-link>
              <router-link class="nav-link" to="/login">Login</router-link>
            </div>
            <div class='d-flex' v-else>
              <div @keyup.enter="searchMovie" id="searchbox">
                <input type="text" v-model="search" id="searchInput" placeholder='영화 제목을 입력하세요' onfocus="this.placeholder=''" onblur="this.placeholder='영화 제목을 입력하세요'">
                <i @click="searchMovie" class="bi bi-search"></i>
              </div>
              <router-link :to="`/profile/detail/${username}`">
                <img class="profileimg" v-if="!profileimg" src="@/assets/user.png" alt="">
                <img class="profileimg" v-else :src=profileimg>
              </router-link >
              <span id="logout" @click="logout">로그아웃</span>
            </div>
          </ul>
        </nav>
      </div>
    </header>

    <section>
      <router-view />
    </section>
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
    },
    profileimg() {
      if (this.$store.state.profileimg) {
        return `http://127.0.0.1:8000` + this.$store.state.profileimg    
      } else {
        return null
      }
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
      const search = this.search
      if (!search) {
        alert('검색어를 입력해주세요')
        return
      }
      const currentKeyword = this.search;
      const previousKeyword = this.$route.query.keyword || '';

      if (currentKeyword !== previousKeyword) {
        const newFullPath = `/search?keyword=${currentKeyword}`;

        if (this.$route.fullPath !== newFullPath) {
          this.$router.push(newFullPath).catch(() => {});
        }
      }
    },
  },
}
</script>

<style scoped>
/* .nav-link {
  font-family: 'Noto Sans KR', sans-serif;
} */

#logo {
  width: 60px;
  margin-left: 10px;
  margin-right: 10px;
}


.profileimg {
  border-radius: 50%;
  height: 32px;
  width: 32px;
  margin-right: 10px;
}


#searchInput {
  border: none;
  border-bottom: solid 2px rgb(196, 196, 196);
}

#searchInput:focus {
  outline: none;
}

#searchbox {
  position: relative;
  margin-right: 15px;
}

i {
  position: absolute;
  right: 6px
}


/*--------------------------------------------------------------
# Header
--------------------------------------------------------------*/
#header {
  /* display: flex;
  flex-direction: row; */
  z-index: 997;
  overflow-y: auto;
  background-color: white;
}
.fixed-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 997;
}

section {
  padding-top: 58px;
}


/*--------------------------------------------------------------
# Navigation Menu
--------------------------------------------------------------*/
/**
* Desktop Navigation 
*/
ul {
  display: flex;
}

nav {
  padding: 30px;
  display: flex;
  direction: row;
  justify-content: space-between;
  padding: 58px;
}
nav div a,
nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav #logout:hover,
nav a:hover {
  color: #35e888;
}

.navbar {
  padding: 0;
  /* margin-top: 35px; */
  /* display: flex;
  direction: row;
  justify-content: space-between;
   */

}

.navbar ul {
  margin-right: 10px;
  margin-left: 10px;
  margin-top: 10px;

  padding: 0;
  list-style: none;
  align-items: center;
}

.navbar #logout,
.navbar div a,
.navbar a {
  position: relative;
  
}

.navbar a+a {
  margin-left: 20px;
  
}
.navbar div a,
.navbar div a:focus,
.navbar #logout,
.navbar #logout:focus,
.navbar a,
.navbar a:focus {
  display: flex;
  direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0;
  /* font-family: "Poppins", sans-serif;*/
  font-family: 'TheJamsil';
  font-size: 16px;
  font-weight: 400;
  /* color: rgba(255, 255, 255, 0.7); */
  white-space: nowrap;
  transition: 0.3s;
}

.navbar #logout:before,
.navbar .nav-link:before {
  content: "";
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -4px;
  left: 0;
  background-color: #18d26e;
  visibility: hidden;
  width: 0px;
  transition: all 0.3s ease-in-out 0s;

}
.navbar div a:hover:before,
.navbar #logout:hover:before,
.navbar a:hover:before{
  visibility: visible;
  width: 100%;
}

ul a {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>