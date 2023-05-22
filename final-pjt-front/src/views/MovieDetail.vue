<template>
  <div>
    <div class="background" :style="{ 'background-image': `url(https://image.tmdb.org/t/p/original/${this.backdrops})` }">
    </div>

      <nav>
        네비게이션셔녓녀
      </nav>
      <div id="hahahaha" v-if="this.movie" style="opacity: 1;">
        <input @click="likewithForm" type="button" :value=likevalue>
        <p>좋아요 수 : {{ like_users_cnt }}</p>
        <p>상세정보</p>
        <img :src=poster_path alt="">
        <p>{{ this.movie.title }}</p>
        <p>{{ this.movie.overview }}</p>
        <p>{{ this.movie.runtime }}분</p>
        <p>{{ this.vote_average }}</p>
        <p>{{ this.movie.release_date }}</p>
        <p>{{ this.movie.production_companies[0]?.name }}</p>
        <span v-for="gen in this.genres_name" :key="gen">{{ gen }},</span>

        <MovieDetailCast v-for="cast in this.cast_list_ko" :key="cast" :cast="cast"
          :original_language="original_language" />
        <MovieDetailReview :movie_id="movie_id" />
      </div>
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
    }
  },
  computed: {
    movieInfo() {
      return this.$store.state.movie_info.id
    },
  },
  methods: {
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
          {
            console.log(res.data.backdrops)
            for (let backdop_path of res.data.backdrops) {
              this.movie_imgs.push(backdop_path.file_path)
              if (this.movie_imgs.length === 15) {
                break
              }
            }
          }
        })
    }
  },
  created() {
    this.getMovieInfo()
  },
  mounted() {
    // 컴포넌트가 마운트될 때 이미지 경로를 가져오는 메소드를 호출합니다.


    // 5초마다 updateBackdrops 메소드를 호출하여 backdrops 값을 업데이트합니다.
    setInterval(() => {
      this.updateBackdrops();
    }, 5000);
  },
  watch: {
    movie_imgs() {
      // movie_imgs 배열이 변경될 때마다 updateBackdrops 메소드를 호출하여 backdrops 값을 업데이트합니다.
      this.updateBackdrops();
    }
  }
}
</script>

<style scoped>
img {
  width: 200px;
}
.background {
  display: block;
  width: 100%;
  height: 100%;
  position: absolute;
  background: top right no-repeat ;
  background-size: contain;
  background-attachment: fixed;
  z-index: -1;
  opacity: 0.4;
}
#hahahaha {
  z-index: 2;
  opacity: 1;
}
</style>