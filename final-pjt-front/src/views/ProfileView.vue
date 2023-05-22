<template>
  <div>
    <main id="">
    <header id="header" :class="{ 'header-scroll': isHeaderScrolled }">
      <div class="d-flex flex-column">

        <div v-if="user" class="profile">
          <img v-if="imgInfo" :src="imgInfo" alt="" class="img-fluid rounded-circle">
          <img v-else src="@/assets/user.png" alt="" class="img-fluid rounded-circle">
          <h1 class="t-white">환영합니다</h1>
          <h1 class="t-white">{{ user.username }}님</h1>
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
  </main>
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
      isHeaderScrolled: false,
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
          if (this.user.profileimg) {
            this.imgInfo = `http://127.0.0.1:8000` + this.user.profileimg
          }
          this.changeProfile()
        })
    },
    changeProfile() {
      const userInfo = this.user
      this.$store.dispatch('changeProfile', userInfo)
    },
    handleScroll() {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      this.isHeaderScrolled = scrollTop > 0
    },
  },
  created() {
    this.getUserProfile()
    window.addEventListener('scroll', this.handleScroll)
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll)
  },

}
</script>

<style scoped>
.t-white {
  color: #e6e6e6;
}


#main {
  margin-left: 300px;
}

@media (max-width: 1199px) {
  #header {
    left: -300px;
  }

  #main {
    margin-left: 0;
  }
}

#header {
  position: fixed;
  top: 57.5px;
  left: 0;
  bottom: 0;
  width: 300px;
  transition: all ease-in-out 0.5s;
  z-index: 9997;
  transition: all 0.5s;
  padding: 0 15px;
  background: #040b14;
  overflow-y: auto;
  transition: all ease-in-out 0.5s;
}

.header-scroll {
  top: 0px;
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

@media (max-width: 1200px) {
  #header {
    display: none;
  }
}

/*--------------------------------------------------------------
# Navigation Menu
--------------------------------------------------------------*/
/* Desktop Navigation */
.nav-menu {
  padding: 30px 0 0 0;
}

.nav-menu * {
  margin: 0;
  padding: 0;
  list-style: none;
}

.nav-menu>ul>li {
  position: relative;
  white-space: nowrap;
}

.nav-menu a,
.nav-menu a:focus {
  display: flex;
  align-items: center;
  color: #a8a9b4;
  padding: 12px 15px;
  margin-bottom: 8px;
  transition: 0.3s;
  font-size: 15px;
}

.nav-menu a i,
.nav-menu a:focus i {
  font-size: 24px;
  padding-right: 8px;
  color: #6f7180;
}

.nav-menu a:hover,
.nav-menu .active,
.nav-menu .active:focus,
.nav-menu li:hover>a {
  text-decoration: none;
  color: #fff;
}

.nav-menu a:hover i,
.nav-menu .active i,
.nav-menu .active:focus i,
.nav-menu li:hover>a i {
  color: #149ddd;
}
</style>