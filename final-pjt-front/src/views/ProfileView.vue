<template>
  <div>
    <header id="header">
      <div class="d-flex flex-column">

        <div v-if="this.user" class="profile">
          <img :src="imgInfo" alt="" class="img-fluid rounded-circle">
          <h1 class="text-light"><a href="index.html">{{ user.nickname }}</a></h1>
          <div class="social-links mt-3 text-center">
          </div>
        </div>

        <nav id="navbar" class="nav-menu navbar">
          <ul>
            <li><a href="#hero" class="nav-link scrollto active"><i class="bx bx-home"></i> <span>♥</span></a></li>
            <li><a href="#about" class="nav-link scrollto"><i class="bx bx-user"></i> <span>About</span></a></li>
            <li><a href="#portfolio" class="nav-link scrollto"><i class="bx bx-book-content"></i>
                <span>LIKE MOVIES</span></a></li>
            <div v-if="this.$route.params.username === this.$store.state.username">
              <li><router-link to="/profile/update" href="#about" class="nav-link scrollto"><i class="bx bx-user"></i>
                  <span>내 정보 수정</span></router-link></li>

            </div>
          </ul>
        </nav>
      </div>
    </header>
    <router-view />
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      user: null,
      imgInfo: null,
    }
  },
  methods: {
    getUserProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/about/${this.$store.state.username}/profile/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.user = res.data
          this.imgInfo = `http://127.0.0.1:8000/` + this.user.profileimg
          this.changeProfile()
        })
    },
    changeProfile() {
      const userInfo = this.user
      this.$store.dispatch('changeProfile', userInfo)
    }
  },
  created() {
    this.getUserProfile()
  }
}
</script>

<style>
#header {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 300px;
  transition: all ease-in-out 0.5s;
  z-index: 9997;
  transition: all 0.5s;
  padding: 0 15px;
  background: #040b14;
  overflow-y: auto;
}

#header .profile img {
  margin: 15px auto;
  display: block;
  width: 120px;
  height: 120px;
  border: 8px solid #2c2f3f;
}

#header .profile h1 {
  font-size: 24px;
  margin: 0;
  padding: 0;
  font-weight: 600;
  -moz-text-align-last: center;
  text-align-last: center;
  font-family: "Poppins", sans-serif;
}

#header .profile h1 a,
#header .profile h1 a:hover {
  color: #fff;
  text-decoration: none;
}
</style>