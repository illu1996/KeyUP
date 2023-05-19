<template>
  <div class="container page-container">
  <div class="row">
    이달의 신작 <button>더보기</button>
    <MainLatestListItem class="col-4" v-for="movie in movieList" :key="movie.id" :movie="movie" />
  </div>
</div>
</template>

<script>
import axios from 'axios';
import MainLatestListItem from './MainLatestListItem.vue'


export default {
  name: 'MainLatestList',
  components: {
    MainLatestListItem,
  },
  data() {
    return {
      movieList: [],
    }
  },
  methods: {
    getPopularMovie() {
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
  computed: {

  },
  created() {
    this.getPopularMovie()
  }
}
</script>

<style></style>
