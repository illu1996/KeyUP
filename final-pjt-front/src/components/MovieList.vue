<template>
  <div>
    MovieList
    <MovieListItem v-for="randomMovie in randomMovieList" :key="randomMovie.movie_id" :randomMovie="randomMovie" />
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
      this.randomMovieList = _.sampleSize(this.movieList, 20)
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

<style></style>