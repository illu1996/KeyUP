<template>
  <div>
    <div>
      관련된 영화
    </div>
    키워드와 관련된 영화 제목은 총    개 입니다.

    <div v-if="this.movieList">
      <SearchMovieList v-for="movie in movieList" :key="movie.id" :movie="movie" />
    </div>

  </div>
</template>

<script>
import SearchMovieList from '@/components/SearchMovieList.vue'
import axios from 'axios';
// import _ from 'lodash'
const MY_URL = 'http://127.0.0.1:8000'


export default {
  name: 'SearchView',
  components: {
    SearchMovieList,
  },
  data() {
    return {
      keyword: this.$route.query.keyword,
      movieList :[]
    }
  },
  watch: {
    $route(to) {
      this.keyword = to.params.keyword;
      this.searchMovie();
    },
  },
  methods:{
    searchMovie(keyword){
      axios({
        method: "GET",
        url: `${MY_URL}/movies/keywords/${keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.movieList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.searchMovie(this.keyword)
  },
}
</script>

<style></style>