<template>
  <div class="container">
    <div class="row">
      <div class="col-5">
        <div v-for="(movie, index) in randomMovieList" :key="index">
          <MovieListItem :class="`lst${index}`" v-if="index === 10" :movie="movie" />
        </div>

        <div class="row">
          <div class="col-6" v-for="(movie, index) in randomMovieList" :key="index">
            <MovieListItem v-if="index === 0" :movie="movie" />
            <MovieListItem v-if="index === 1" :movie="movie" />
            <MovieListItem v-if="index === 2" :movie="movie" />
            <MovieListItem v-if="index === 3" :movie="movie" />
          </div>
          <!-- <div class="col-4" v-for="(movie, index) in randomMovieList" :key="index"> -->

          <!-- </div> -->
          <!-- <div class="col box2"></div> -->
          <!-- <div class="row">
            <div class="col box3"></div>
            <div class="col box4"></div>
          </div> -->
        </div>
      </div>
      <div class="col">
        <div class="col-6">
          <div v-for="(movie, index) in randomMovieList" :key="index">
            <MovieListItem :class="`lst${index}`" v-if="index === 3" :movie="movie" />
          </div>
          <div v-for="(movie, index) in randomMovieList" :key="index">
            <MovieListItem :class="`lst${index}`" v-if="index === 4" :movie="movie" />
          </div>

          <!-- <div class="col box2"></div> -->
          <!-- <div class="row">
            <div class="col box3"></div>
            <div class="col box4"></div>
          </div> -->
        </div>
        <div class="col">
          <div v-for="(movie, index) in randomMovieList" :key="index">
            <MovieListItem :class="`lst${index}`" v-if="index === 5" :movie="movie" />
          </div>
        </div>

      </div>
      <div class="col-4 box4"></div>
      <div class="row box1"></div>
      <div class="row box1"></div>

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
      randomMovieList: []
    }
  },
  methods: {
    randomList() {
      this.randomMovieList = _.sampleSize(this.movieList, 11)
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

<style scoped>
</style> 
