<template>
  <div class="container">
    <div class="row">
    <LatestListItem class="col-4" v-for="movie in movieList" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import LatestListItem from './LatestListItem.vue'
export default {
  name:'LatestList',
  components : {
    LatestListItem,
  },
  data() {
    return {
      movieList: [],
    }
  },
  methods: {
    getLatestMovie() {
      axios({
        method: 'get',
        url: "https://api.themoviedb.org/3/movie/now_playing?language=ko-kr&page=1",
        headers: {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        }
      })
        .then((res) => {
          console.log(res.data)
          this.movieList = res.data.results
        })
    }

  },
  created() {
    this.getLatestMovie()
  }
}
</script>

<style>

</style>