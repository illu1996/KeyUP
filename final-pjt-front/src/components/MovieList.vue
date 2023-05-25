<template>
  <div class="container">
    <div class="row">
      <div class="col-5">
        <div class="row movie-item">
          <MovieListItem v-for="movie in movieList.slice(4, 5)" :key="movie.id" :movie="movie" />
        </div>
        <div class="row movie-item">
          <MovieListItem class="col-6" v-for="movie in movieList.slice(0, 4)" :key="movie.id" :movie="movie" />
        </div>

        <div class="row movie-item">
          <MovieListItem v-for="movie in movieList.slice(5, 6)" :key="movie.id" :movie="movie" />
        </div>
      </div>
      <div class="col-3 movie-item">
        <MovieListItem class="col" v-for="movie in movieList.slice(6, 11)" :key="movie.id" :movie="movie" />
      </div>
      <div class="col-4 movie-item">
        <MovieListItem class="col" v-for="movie in movieList.slice(11, 15)" :key="movie.id" :movie="movie" />
      </div>
    </div>
    <div v-if="isLoading">
      <div class="spinner-border text-dark" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'
import axios from 'axios'

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

      isLoading: true,
    }
  },
  methods: {
    randomList() {

      this.isLoading = false
    },
    getMovieList() {
      axios({
        method: "GET",
        url: `${MY_URL}/movies/`
      })
        .then((res) => {
          this.movieList = res.data
          this.randomList()
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
.spinner-border {
  margin: 50px;
}

.loader1 {
  position: relative;
  height: 80px;
  width: 80px;
  border-radius: 80px;
  border: 3px solid rgba(228, 11, 11, 0.7);

  top: 28%;
  top: -webkit-calc(50% - 43px);
  top: calc(50% - 43px);
  left: 35%;
  left: -webkit-calc(50% - 43px);
  left: calc(50% - 43px);

  -webkit-transform-origin: 50% 50%;
  transform-origin: 50% 50%;
  -webkit-animation: loader1 3s linear infinite;
  animation: loader1 3s linear infinite;
}

.loader1:after {
  content: "";
  position: absolute;
  top: -5px;
  left: 20px;
  width: 11px;
  height: 11px;
  border-radius: 10px;
  background-color: rgba(228, 11, 11, 0.7);
}

@-webkit-keyframes loader1 {
  0% {
    -webkit-transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
  }
}

@keyframes loader1 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style> 
