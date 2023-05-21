<template>
  <div>
    <div v-if="userInfo && this.$store.state.username != userInfo.username">

      <button v-if="!followers.includes(this.$store.state.username)" @click="follow">팔로우</button>
      <button v-else @click="follow">팔로우 취소</button>

    </div>
    <p>팔로워 : {{ follower }} | 팔로잉 : {{ following }}</p>
    <p>닉네임 : {{ userInfo?.nickname }}</p>
    <p>소개말 : {{ userInfo?.introduce }}</p>
    <p>좋아요 한 영화</p>



    <!-- ======= Hero Section ======= -->
    <section id="hero" class="d-flex flex-column justify-content-center align-items-center" :style="heroBackground">
      <div class="hero-container" data-aos="fade-in">
        <h1>{{ userInfo?.nickname }}</h1>
        <p>I'm <span class="typed" data-typed-items="Designer, Developer, Freelancer, Photographer"></span></p>
      </div>
    </section><!-- End Hero -->

    <main id="main">

      <!-- ======= About Section ======= -->
      <section id="about" class="about">
        <div class="container">

          <div class="section-title">
            <h2>About</h2>
            <p>Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint
              consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit
              in iste officiis commodi quidem hic quas.</p>
          </div>

          <div class="row">
            <div class="col-lg-4" data-aos="fade-right">
              <img :src=imgInfo class="img-fluid" alt="">
            </div>
            <div class="col-lg-8 pt-4 pt-lg-0 content" data-aos="fade-left">
              <h3>UI/UX Designer &amp; Web Developer.</h3>
              <p class="fst-italic">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                dolore
                magna aliqua.
              </p>
              <div class="row">
                <div class="col-lg-6">
                  <ul>
                    <li><i class="bi bi-chevron-right"></i> <strong>Birthday:</strong> <span>1 May 1995</span></li>
                    <li><i class="bi bi-chevron-right"></i> <strong>Website:</strong> <span>www.example.com</span></li>
                    <li><i class="bi bi-chevron-right"></i> <strong>Phone:</strong> <span>+123 456 7890</span></li>
                    <li><i class="bi bi-chevron-right"></i> <strong>City:</strong> <span>New York, USA</span></li>
                  </ul>
                </div>
                <div class="col-lg-6">
                  <ul>
                    <li><i class="bi bi-chevron-right"></i> <strong>Age:</strong> <span>30</span></li>
                    <li><i class="bi bi-chevron-right"></i> <strong>Degree:</strong> <span>Master</span></li>
                    <li><i class="bi bi-chevron-right"></i> <strong>PhEmailone:</strong> <span>email@example.com</span>
                    </li>
                    <li><i class="bi bi-chevron-right"></i> <strong>Freelance:</strong> <span>Available</span></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

        </div>
      </section><!-- End About Section -->

      <!-- ======= Portfolio Section ======= -->
      <section id="portfolio" class="portfolio section-bg">
        <div class="container">


          <div class="row portfolio-container" data-aos="fade-up" data-aos-delay="100">
            <div v-for="(movie, index) in movielist" :key="index" @click="changeMovie(movie)"
              class="col-lg-4 col-md-6 portfolio-item filter-card">
              <div class="portfolio-wrap">
                <p>{{ movie.title }}</p>
                <img :src="getImageUrl(movie.poster_path)" class="img-fluid">
              </div>
            </div>

          </div>

        </div>
      </section><!-- End Portfolio Section -->

    </main><!-- End #main -->

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
  computed: {
    heroBackground() {
      return {
        'background': `url(${this.imgInfo}) top center`,
        'background-size': 'cover',
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
          this.movielist = []; // 기존 영화 목록 초기화
          this.getMovies();
        }
      }
    }
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
            if (this.userInfo.profileimg) {
              this.imgInfo = `http://127.0.0.1:8000/` + this.userInfo.profileimg
            }
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
          console.log(res.data)
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
          console.log(res.data.person.followers)
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


/*--------------------------------------------------------------
# Hero Section
--------------------------------------------------------------*/
#hero {
  position: relative;
  width: 100%;
  height: 100vh;
  background-size: cover;
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
  margin-bottom: 50px;
  font-size: 26px;
  font-family: "Poppins", sans-serif;
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

.portfolio .portfolio-wrap .portfolio-links {
  opacity: 1;
  left: 0;
  right: 0;
  bottom: -60px;
  z-index: 3;
  position: absolute;
  transition: all ease-in-out 0.3s;
  display: flex;
  justify-content: center;
}

.portfolio .portfolio-wrap .portfolio-links a {
  color: #fff;
  font-size: 28px;
  text-align: center;
  background: rgba(20, 157, 221, 0.75);
  transition: 0.3s;
  width: 50%;
}

.portfolio .portfolio-wrap .portfolio-links a:hover {
  background: rgba(20, 157, 221, 0.95);
}

.portfolio .portfolio-wrap .portfolio-links a+a {
  border-left: 1px solid #37b3ed;
}

.portfolio .portfolio-wrap:hover::before {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 1;
}

.portfolio .portfolio-wrap:hover .portfolio-links {
  opacity: 1;
  bottom: 0;
}

/*--------------------------------------------------------------
# Portfolio Details
--------------------------------------------------------------*/
.portfolio-details {
  padding-top: 40px;
}

.portfolio-details .portfolio-details-slider img {
  width: 100%;
}

.portfolio-details .portfolio-details-slider .swiper-pagination {
  margin-top: 20px;
  position: relative;
}

.portfolio-details .portfolio-details-slider .swiper-pagination .swiper-pagination-bullet {
  width: 12px;
  height: 12px;
  background-color: #fff;
  opacity: 1;
  border: 1px solid #149ddd;
}

.portfolio-details .portfolio-details-slider .swiper-pagination .swiper-pagination-bullet-active {
  background-color: #149ddd;
}

.portfolio-details .portfolio-info {
  padding: 30px;
  box-shadow: 0px 0 30px rgba(5, 13, 24, 0.08);
}

.portfolio-details .portfolio-info h3 {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.portfolio-details .portfolio-info ul {
  list-style: none;
  padding: 0;
  font-size: 15px;
}

.portfolio-details .portfolio-info ul li+li {
  margin-top: 10px;
}

.portfolio-details .portfolio-description {
  padding-top: 30px;
}

.portfolio-details .portfolio-description h2 {
  font-size: 26px;
  font-weight: 700;
  margin-bottom: 20px;
}

.portfolio-details .portfolio-description p {
  padding: 0;
}
</style>
