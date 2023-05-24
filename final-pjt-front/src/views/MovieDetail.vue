<template>
  <div>
    <main id="main">
      <header id="header" :class="{ 'header-scroll': isHeaderScrolled }">
        <div class="d-flex flex-column">
          <nav id="navbar" class="nav-menu navbar">
            <ul>
              <li><a href="#background" class="nav-link scrollto active"><i class="bx bx-home"></i> <span>Image</span></a>
              </li>
              <li><a href="#about" class="nav-link scrollto"><i class="bx bx-user"></i> <span>About</span></a></li>
              <li><a href="#cast" class="nav-link scrollto"><i class="bx bx-book-content"></i><span>Cast</span></a></li>
              <li><a href="#review" class="nav-link scrollto"><i class="bx bx-book-content"></i><span>Reviews</span></a>
              </li>
            </ul>
          </nav>
        </div>
      </header>
      <div class="information" v-if="this.movie">
        <div class="background" id="background"
        :style="{ 'background-image': `url(https://image.tmdb.org/t/p/original/${this.backdrops})` }" >
        </div>
        <section id="hero" class="d-flex flex-column justify-content-center align-items-center" >
          <div class="hero-container" data-aos="fade-in">
            <h1>{{ this.movie.title }}</h1>
          </div>
        </section>

        <section id="about" class="about">
          <div class="container">
            <div class="section-title">
              <h2>영화 정보</h2>
            </div>
            <div class="row">
              <div class="col-lg-4" data-aos="fade-right">
                <img :src=poster_path alt="" style="width:80%">
              </div>
              <div class="col-lg-8 pt-4 pt-lg-0 content" data-aos="fade-left">
                <h3>{{ this.movie.title }}</h3>
                <div class="row">
                  <div class="col-lg-12">
                    <ul class="no_dot">
                      <li><i class="bi bi-chevron-right"></i> <strong>개봉일 :</strong> <span>{{ this.movie.release_date
                      }}</span></li>
                      <li><i class="bi bi-chevron-right"></i> <strong>평점 :</strong> <span>{{ this.vote_average }}</span>
                      </li>
                      <li><i class="bi bi-chevron-right"></i> <strong>장르 :</strong>
                        <span v-for="(gen, index) in this.genres_name" :key="index">
                          <span> {{ gen }}</span>
                          <span v-if="index !== genres_name.length - 1">,</span>
                        </span>
                      </li>

                      <li><i class="bi bi-chevron-right"></i> <strong>상영시간 :</strong> <span>{{ this.movie.runtime }}분
                        </span></li>
                      <li v-if="this.movie.production_companies"><i class="bi bi-chevron-right"></i> <strong>제작사
                          :</strong> <span>{{
                            this.movie.production_companies[0]?.name }}</span></li>
                      <li><i class="bi bi-chevron-right"></i> <strong>줄거리 :</strong> <span>{{ this.movie.overview
                      }}</span>
                      </li>
                      <br>
                      <br>
                      <div class="d-flex justify-content-center"> <input @click="likewithForm" type="button" :value=likevalue>
                        <p>좋아요 수 : {{ like_users_cnt }}</p>
                      </div>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section><!-- End About Section -->
        <br>
        <br>
        <section id="cast" class="cast">
          <br>
          <br>
          <br>
          <div class="container">
            <div class="section-title">
              <h2>캐스트</h2>
            </div>
            <div class="row">
              <MovieDetailCast class="col-2" v-for="(cast, index) in this.cast_list_ko" :key="index" :cast="cast" :index="index"
                :original_language="original_language" />
            </div>
          </div>
        </section>

        <section id="review" class="review">
          <div class="container">
            <div class="section-title">
              <h4>코멘트</h4>
            </div>
            <div class="commentbox">
              <MovieDetailReview class="container" :movie_id="movie_id" />
            </div>
          </div>
        </section>

      </div>


    </main>
  </div>
</template>

<script>
import axios from 'axios';
import MovieDetailCast from '@/components/MovieDetailCast.vue'
import MovieDetailReview from '@/components/MovieDetailReview.vue'
const MY_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetail',
  components: {
    MovieDetailCast,
    MovieDetailReview,
  },
  data() {
    return {
      title: null,
      movie: null,
      genres: null,
      poster_path: null,
      vote_average: null,
      genres_name: [],
      movie_id: null,
      original_language: null,
      cast_list_ko: [],
      cast_list: [],
      likevalue: null,
      like_users_cnt: 0,
      like_users: [],
      movie_imgs: [],
      backdrops: null,
      isHeaderScrolled: false,
    }
  },
  computed: {
    movieInfo() {
      return this.$store.state.movie_info.id
    },
  },
  methods: {
    handleScroll() {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      this.isHeaderScrolled = scrollTop > 0
    },
    updateBackdrops() {
      if (this.movie_imgs.length > 0) {
        const currentIndex = this.movie_imgs.indexOf(this.backdrops);
        const nextIndex = (currentIndex + 1) % this.movie_imgs.length;
        this.backdrops = this.movie_imgs[nextIndex];
      }
    },
    getLike() {
      axios({
        method: 'get',
        url: `${MY_URL}/movies/${this.movie_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          // movie_id : this.movie.movie_id,
          // adult:this.movie.adult,
          // title:this.movie.title,
          // original_title: this.movie.original_title,
          // overview :this.movie.overview,
          // poster_path :this.movie.poster_path,
          // release_date :this.movie.release_date,
          // vote_average: this.movie.vote_average,
          // vote_count:this.movie.vote_count
        }
      })
        .then((res) => {
          console.log(res.data)

          this.like_users_cnt = res.data.like_users_cnt
          this.like_users = res.data.like_users
          if (res.data.like_users.includes(this.$store.state.username)) {
            this.likevalue = '좋아요 취소'
          }
          else {
            this.likevalue = '좋아요'
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    likewithForm() {
      axios({
        method: 'post',
        url: `${MY_URL}/movies/${this.movie_id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        // data:{
        //   id:1
        // }
      })
        .then((res) => {
          console.log(res.data)
          console.log(this.$store.state.username)

          this.like_users_cnt = res.data.like_users_cnt
          this.like_users = res.data.like_users
          if (res.data.like_users.includes(`${this.$store.state.username}`)) {
            this.likevalue = '좋아요 취소'
          }
          else {
            this.likevalue = '좋아요'
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getImage() {
      this.poster_path = `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
    getMovieInfo() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieInfo}?language=ko-kr`,
        headers: {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        },
      })
        .then((res) => {
          console.log(res.data)
          this.original_language = res.data.original_language
          this.movie_id = res.data.id
          this.movie = res.data
          this.title = res.data.title
          this.getImage()
          this.getImagesPath()
          console.log(this.movie_imgs)
          this.getLike()
          this.vote_average = Math.round(res.data.vote_average * 10) / 10
          for (let genre of res.data.genres) {
            if (genre.name) {
              this.genres_name.push(genre.name)
            }
          }
          this.getMovieCredit()
        })
    },
    getMovieCredit() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie_id}/credits?language=ko-kr`,
        headers: {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        }
      })
        .then((res) => {
          {
            for (let crew of res.data.crew) {
              if (crew.department === "Directing") {
                this.cast_list_ko.push(crew.id)
                break
              }
            }
            for (let cast of res.data.cast.slice(0, 5)) {
              if (!this.cast_list_ko.includes(cast.id)) {
                this.cast_list_ko.push(cast.id)
              }
            }
          }
        })
    },
    getImagesPath() {
      this.movie_imgs = []
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie_id}/images`,
        headers: {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYmFkZTM0OTMyZWU0MmViZWU1YzhjMTRmYjEyZmVkMyIsInN1YiI6IjYzZDMxN2U2MDMxYTFkMDBjMDk1NDllYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c0wwyJxR1feCAcNSyuF6bbLE_FyqZvCwbgZYRDAL3L8"
        }
      })
        .then((res) => {
          console.log(res.data)
          {
            console.log(res.data.backdrops)
            for (let backdrop_path of res.data.backdrops) {
              if (backdrop_path.iso_639_1 === 'en' || backdrop_path.iso_639_1 === "ko" || backdrop_path.iso_639_1 === null)
                this.movie_imgs.push(backdrop_path.file_path)
              if (this.movie_imgs.length === 15) {
                break
              }
            }
          }
        })
    }
  },
  watch: {
    movie_imgs() {
      // movie_imgs 배열이 변경될 때마다 updateBackdrops 메소드를 호출하여 backdrops 값을 업데이트합니다.
      this.updateBackdrops();
    }
  },
  created() {
    this.getMovieInfo()
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted() {
    // 5초마다 updateBackdrops 메소드를 호출하여 backdrops 값을 업데이트합니다.
    setInterval(() => {
      this.updateBackdrops();
    }, 5000);
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>

<style scoped>

.commentbox {
  /* box-sizing: content-box; */
  border: solid 1px rgb(187, 187, 187);
}

.review {
  margin-top: 50px;
}

.no_dot {
  list-style-type: none;
}

.no_dot i {
  color: #149ddd;
}

main {
  margin: 0px;
}

ul {
  margin: 0px;
}

li {
  margin: 0px;
}

img {
  width: 200px;
}



#main {
  position: relative;
  /* margin-left: 200px; */
  background-attachment: scroll;
}

@media (max-width: 1199px) {
  #header {
    left: -200px;
  }

  #main {
    margin-left: 0;
  }
}

#header {
  position: fixed;
  top: 59px;
  left: 0;
  bottom: 0;
  width: 200px;
  transition: all ease-in-out 0.5s;
  z-index: 9997;
  transition: all 0.5s;
  padding: 0 15px;
  background: #040b14;
  overflow-y: auto;
  transition: all ease-in-out 0.5s;
  opacity: 1;
}


/*--------------------------------------------------------------
# Navigation Menu
--------------------------------------------------------------*/
/* Desktop Navigation */
.nav-menu {
  padding: 30px;

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

.section-title h2{
  margin-top: 30px;
  margin-bottom : 20px;
}
.information {
  position: relative;
  margin-left: 200px;
}
#hero {
  width: 100%;
  height: 100vh;

}

.background{
  box-sizing: border-box;
  margin: 0px;
  padding: 0px;
  width: 100%;
  height: 100vh;
  position: absolute;
  background: top right no-repeat;
  background-size: cover;
  background-attachment: fixed;
  z-index: 1;
  opacity: 0.8;
}
.background:before {
  content: "";
  background: rgba(5, 13, 24, 0.6);
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
  font-size: 80px;
  font-weight: 700;
  line-height: 56px;
  color: #ffffff;
}
</style>