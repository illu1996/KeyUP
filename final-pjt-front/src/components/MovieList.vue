<template>
  <div class="container">
    <div class="row">
      <div class="col-5">
        <div class="row">
        <MovieListItem v-for="movie in randomMovieList.slice(4,5)" :key="movie.id" :movie="movie"/>
      </div>
        <div class="row">
          <MovieListItem class="col-6" v-for="movie in randomMovieList.slice(0,4)" :key="movie.id" :movie="movie" />
          </div>

          <div class="row">
        <MovieListItem v-for="movie in randomMovieList.slice(5,6)" :key="movie.id" :movie="movie"/>
      </div>
    </div>
      <div class="col-3">
        <MovieListItem class="col" v-for="movie in randomMovieList.slice(6,11)" :key="movie.id" :movie="movie" />
      </div>
      
      <div class="col-4">
        <MovieListItem class="col" v-for="movie in randomMovieList.slice(11,15)" :key="movie.id" :movie="movie" />
      </div>

    </div>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'
import axios from 'axios'
import _ from 'lodash'
const MY_URL = 'http://127.0.0.1:8000'
// const MY_KEY =''


export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data() {
    return {
      movieList: [],
      randomMovieList: [],
    }
  },
  methods: {
    randomList() {
      this.randomMovieList = _.sampleSize(this.movieList, 15)

    },
    getMovieList() {
      axios({
        method: "GET",
        url: `${MY_URL}/movies/`
      })
        .then((res) => {
          this.movieList = res.data
          this.randomList()
          console.log(this.randomMovieList)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getMovieList()

  }
}
</script>

<style scoped></style> 
