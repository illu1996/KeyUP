<template>
  <div>
    <div v-if="this.movie">
      <p>상세정보</p>
      <img :src=poster_path alt="">
      <p>{{ this.title.movie }}</p>
      <p>{{ this.movie.overview }}</p>
      <p>{{ this.movie.runtime }}분</p>
      <p>{{ this.vote_average }}</p>
      <p>{{ this.movie.release_date }}</p>
      <p>{{ this.movie.production_companies[0].name }}</p>
      <span v-for="gen in this.genres_name" :key="gen">{{ gen }},</span>
      
      <MovieDetailCast v-for="cast in this.cast_list_ko" :key="cast" :cast="cast" :original_language="original_language"/>
      <MovieDetailReview :movie_id="movie_id"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import MovieDetailCast from '@/components/MovieDetailCast.vue'
import MovieDetailReview from '@/components/MovieDetailReview.vue'

export default {
  name: 'MovieDetail',
  components:{
    MovieDetailCast,
    MovieDetailReview,
  },
  data() {
    return {
      movie : null,
      genres : null,
      poster_path : null,
      vote_average : null,
      genres_name : [],
      movie_id : null,
      original_language : null,
      cast_list_ko : [],
      cast_list : [],
    }
  },
  computed: {
    movieInfo() {
      return this.$store.state.movie_info.id
    },

  },
  methods: {
    getImage() {
      this.poster_path = `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
    getMovieInfo() {
      axios({
        method: 'get',
        url : `https://api.themoviedb.org/3/movie/${this.movieInfo}?language=ko-kr`,
        headers : {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        }
      })
      .then((res) => {
        this.original_language = res.data.original_language
        this.movie_id = res.data.id
        this.movie = res.data
        this.title = res.data.title
        this.getImage()
        this.vote_average = Math.round(res.data.vote_average*10)/10
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
        url : `https://api.themoviedb.org/3/movie/${this.movie_id}/credits?language=ko-kr`,
        headers : {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        }
      })
      .then((res)=>{{
        for (let crew of res.data.crew) {
          if (crew.department === "Directing") {
            this.cast_list_ko.push(crew.id)
            break
          }
        }
        for (let cast of res.data.cast.slice(0, 5)) {
          this.cast_list_ko.push(cast.id)
        }
      }
      })
    }
  },
  created() {
    this.getMovieInfo()
  }
}
</script>

<style scoped>
img {
  width: 200px;
}
</style>