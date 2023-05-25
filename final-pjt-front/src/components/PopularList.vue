<template>
  <div class="container">
    <h1> | 인기작</h1>
    <div class="row">
      <div class="col-6">
        <PopularListItem v-for="(movie,index) in movieList.slice(0, 1)" :key="movie.id" :movie="movie" :index="index+1"/>
      </div>
      <div class="col-3">
        <PopularListItem class="" v-for="(movie,index) in movieList.slice(1, 3)" :key="movie.id" :movie="movie" :index="index+2"/>
      </div>
      <div class="col-3">
        <PopularListItem class="" v-for="(movie,index) in movieList.slice(3, 5)" :key="movie.id" :movie="movie" :index="index+4" />
      </div>

    </div>


    <div class="row">
      <PopularListItem class="col" v-for="(movie,index) in movieList.slice(5, 9)" :key="movie.id" :movie="movie" :index="index+6"/>
    </div>
    <div class="row">
      <PopularListItem class="col" v-for="(movie,index) in movieList.slice(9, 13)" :key="movie.id" :movie="movie" :index="index+10"/>
    </div>
    <div class="row">
      <PopularListItem class="col" v-for="(movie,index) in movieList.slice(13, 17)" :key="movie.id" :movie="movie" :index="index+14"/>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios';

import PopularListItem from './PopularListItem.vue'
export default {
  name: 'PopularList',
  components: {
    PopularListItem,
  },
  data() {
    return {
      movieList: []
    }
  },
  methods: {
    getPopularMovie() {
      axios({
        method: 'get',
        url: "https://api.themoviedb.org/3/movie/popular?language=ko-kr&page=1",
        headers: {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        }
      })
        .then((res) => {
          this.movieList = res.data.results
        })
    }
  },
  created() {
    this.getPopularMovie()
  }
}
</script>

<style scoped>
.container h1 {
  text-align: left;
  margin-bottom: 30px;
}
</style>