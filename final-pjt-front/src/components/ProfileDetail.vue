<template>
  <div>
    <section id="hero" class="d-flex flex-column justify-content-center align-items-center" :style="heroBackground">
      <div class="hero-container" data-aos="fade-in">
        <h1>{{ userInfo?.nickname }}</h1>
        <p><span class="typed" data-typed-items="">{{ userInfo?.introduce }}</span></p>
      </div>
    </section>

    <main id="main">
      <section id="about" class="about">
        <div class="container">

          <div class="row">
            <div class="col-lg-4" data-aos="fade-right">
              <img v-if="imgInfo" :src=imgInfo class="img-fluid" alt="">
              <img v-else class="img-fluid" src="@/assets/default.png" alt="">
            </div>
            <div class="col-lg-8 pt-4 pt-lg-0 content" data-aos="fade-left">
              <div class="followbox d-flex justify-content-between">
                <div>
                  <h3>{{ this.$route.params.username }}님</h3>
                  <div v-if="userInfo && this.$store.state.username != userInfo.username">
                    <button class="gradient-btn" v-if="!followers.includes(this.$store.state.username)"
                      @click="follow">follow</button>
                    <button class="gradient-btn" v-else @click="follow"><i class="bi bi-check2-all"></i></button>
                  </div>
                </div>
                <div class="follownum d-flex text-center">
                  <div>
                    <p>팔로워</p>
                    <p class="follower">{{ follower }}</p>
                  </div>
                  <div>
                    <p>팔로잉</p>
                    <p class="following">{{ following }}</p>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-lg-6">
                  <ul>
                    <li><i class="bi bi-chevron-right"></i> <strong>닉네임 : </strong> <span>{{ userInfo?.nickname }}</span>
                    </li>
                    <li><i class="bi bi-chevron-right"></i> <strong>나의 한마디 : </strong> <span>{{
                      userInfo?.introduce }}</span></li>
                    <li><i class="bi bi-chevron-right"></i> <strong>{{ userInfo?.nickname }}님의 영화</strong> <span></span>
                    </li>
                  </ul>
                </div>
                <section id="portfolio" class="portfolio section-bg">
                  <div class="container">
                    <div class="row portfolio-container" data-aos="fade-up" data-aos-delay="100">
                      <div v-for="(movie, index) in movielist" :key="index" @click="changeMovie(movie)"
                        class="col-lg-3 col-md-6 portfolio-item filter-card">
                        <div class="portfolio-wrap">
                          <img :src="getImageUrl(movie.poster_path)" class="img-fluid">
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProfileDetail',
  data() {
    return {
      movielist: [],
      user: this.$store.state.userInfo,
      imgInfo: null,
      userInfo: null,
      follower: null,
      following: null,
      userName: this.$route.params.username,
      followers: [],
    }
  },
  components: {

  },
  computed: {
    // imgInfo() {
    //   return 'http://127.0.0.1:8000' + this.$store.state.profileimg
    // },
    heroBackground() {
      return {
        'background': `url(${this.imgInfo}) top center`,
        'background-size': 'contain',
        'background-repeat': 'no-repeat',
      };
    },
      
  },
  watch: {
    $route(to) {
      this.userName = to.params.username;
      this.infoOfuser();
    },
    userInfo: {
      immediate: true,
      handler(newValue) {
        if (newValue && newValue.like_movies) {
          this.movielist = [];
          this.getMovies();
        }
      }
    },
    'this.$store.state.profileimg': {
      immediate: true,
      handler() {
        if (this.userInfo && !this.userInfo.profileimg) {
          this.$nextTick(() => {
            this.$forceUpdate();
          });
        }
      }
    },
  },
  methods: {
    changeMovie(movie) {
      const movieinfo = movie
      this.$store.dispatch('changeMovie', movieinfo)
      this.$router.push({ name: 'MovieDetail' })
    },
    getImageUrl(posterPath) {
      return `https://image.tmdb.org/t/p/original/${posterPath}`;
    },
    getMovies() {
      const movies = this.userInfo?.like_movies
      for (let movie of movies) {
        axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/movie/${movie}?language=ko-kr`,
          headers: {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
          }
        })
          .then((res) => {
            const movieData = res.data;
            if (this.movielist.some((movie) => movie.id === movieData.id)) {
              return;
            }
            this.movielist.push(res.data)
          })
      }
    },


    infoOfuser() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/about/${this.$route.params.username}/profile/`
      })
        .then((res) => {
          this.userInfo = res.data
          if (this.userInfo.profileimg) {
              this.imgInfo = `http://127.0.0.1:8000` + this.userInfo.profileimg
            }
          this.getMovies()
          this.creatfollow()
        })
    },

    follow() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/about/${this.userInfo.id}/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((res) => {
          this.follower = res.data.followers_count
          this.following = res.data.followings_count
          this.followers = res.data.person.followers
        })
    },

    creatfollow() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/about/${this.userInfo.id}/follow/`,
      })
        .then((res) => {

          this.follower = res.data.followers_count
          this.following = res.data.followings_count
          this.followers = res.data.person.followers
        })
    },


  },
  created() {
    this.infoOfuser()
  }
}
</script>

<style scoped>
.img-fluid {
  width: auto;
  height: auto;
}

.gradient-btn {
  display: inline-block;
  padding: 0.8em 1.6em;
  width: 100px;
  border-radius: 0;
  color: #040b14;
  font-weight: bold;
  font-size: 0.678rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  text-decoration: none;
  background: linear-gradient(to right, rgba(178, 135, 111, 0) 25%, rgba(65, 73, 129, 0.8) 75%);
  background-position: 1% 50%;
  background-size: 400% 300%;
  border: 1px solid #040b14;
  transition: all 0.3s;
}

.gradient-btn:hover {
  color: white;
  background-position: 99% 50%;
}

.follower,
.following {
  font-weight: 700;
  font-size: 20px;
  margin: 0px;
}

.followbox {
  margin-bottom: 16px;
}

.follownum p {
  margin-left: 10px;
  margin-right: 10px;
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


#hero {
  position: relative;
  width: 100vw;
  height: 500px;
  background-size: cover;
  margin-bottom: 20px;
}

#hero:before {
  content: "";
  background: rgba(5, 13, 24, 0.3);
  position: absolute;
  bottom: 0;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1;
}

#hero .hero-container {
  position: relative;
  z-index: 2;
  min-width: 300px;
}

#hero h1 {
  margin: 0 0 10px 0;
  font-size: 64px;
  font-weight: 700;
  line-height: 56px;
  color: #fff;
}

#hero p {
  color: #fff;
  /* margin-bottom: 50px; */
  font-size: 26px;
  /* font-family: "Poppins", sans-serif; */
}

#hero p span {
  color: #fff;
  padding-bottom: 4px;
  letter-spacing: 1px;
  border-bottom: 3px solid #149ddd;
}

@media (min-width: 1024px) {
  #hero {
    background-attachment: fixed;
  }
}

@media (max-width: 768px) {
  #hero h1 {
    font-size: 28px;
    line-height: 36px;
  }

  #hero h2 {
    font-size: 18px;
    line-height: 24px;
    margin-bottom: 30px;
  }
}


/*--------------------------------------------------------------
# About
--------------------------------------------------------------*/
.about .content h3 {
  font-weight: 700;
  font-size: 26px;
  color: #173b6c;
}

.about .content ul {
  list-style: none;
  padding: 0;
}

.about .content ul li {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}

.about .content ul strong {
  margin-right: 10px;
}

.about .content ul i {
  font-size: 16px;
  margin-right: 5px;
  color: #149ddd;
  line-height: 0;
}

.about .content p:last-child {
  margin-bottom: 0;
}


/*--------------------------------------------------------------
# Portfolio
--------------------------------------------------------------*/
.portfolio .portfolio-item {
  margin-bottom: 30px;
}

.portfolio #portfolio-flters {
  padding: 0;
  margin: 0 auto 35px auto;
  list-style: none;
  text-align: center;
  background: #fff;
  border-radius: 50px;
  padding: 2px 15px;
}

.portfolio #portfolio-flters li {
  cursor: pointer;
  display: inline-block;
  padding: 10px 15px 8px 15px;
  font-size: 14px;
  font-weight: 600;
  line-height: 1;
  text-transform: uppercase;
  color: #272829;
  margin-bottom: 5px;
  transition: all 0.3s ease-in-out;
}

.portfolio #portfolio-flters li:hover,
.portfolio #portfolio-flters li.filter-active {
  color: #149ddd;
}

.portfolio #portfolio-flters li:last-child {
  margin-right: 0;
}

.portfolio .portfolio-wrap {
  transition: 0.3s;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.portfolio .portfolio-wrap::before {
  content: "";
  background: rgba(255, 255, 255, 0.5);
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  transition: all ease-in-out 0.3s;
  z-index: 2;
  opacity: 0;
}

.no_dot {
  list-style-type: none;
}

.portfolio .portfolio-wrap:hover::before {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 1;
}

.portfolio-item .img-fluid {
  height: 100%;
  object-fit: cover;
}</style>
