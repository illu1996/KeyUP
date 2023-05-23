<template>
  <div class="container">
    <div class="keyword-title d-flex column me-2 align-items-center">
      <h2 class="">{{keyword}}</h2> 
      <b class="ms-2">와(과) 관련된 영화 제목은 총 {{ movieList.length }}개 입니다.</b>
    </div>

    <div class="row mt-3" v-if="movieList.length > 0">
      <SearchMovieList class="col-3 mt-2" v-for="movie in movieList" :key="movie.id" :movie="movie"  />
    </div>
  </div>
</template>

<script>
import SearchMovieList from '@/components/SearchMovieList.vue';
import axios from 'axios';


const MY_URL = 'http://127.0.0.1:8000';

export default {
  name: 'SearchView',
  components: {
    SearchMovieList,
  },
  data() {
    return {
      keyword: this.$route.query.keyword,
      movieList: [],
      
    };
  },
  beforeRouteUpdate(to, from, next) {
    if (to.path === from.path && to.query.keyword === from.query.keyword) {
      next(false);
    } else {
      next();
    }
  },
  watch: {
    '$route.query.keyword'(newKeyword) {
      if (newKeyword !== this.keyword) {
        this.keyword = newKeyword;
        this.searchMovie();
      } else {
        const newFullPath = `/search?keyword=${newKeyword}`;
        if (this.$route.fullPath !== newFullPath) {
          this.$router.push(newFullPath).catch(() => {});
        }
      }
    },
  },
  methods: {
    searchMovie() {
      axios({
        method: 'GET',
        url: `${MY_URL}/movies/keywords/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res.data);
          this.movieList = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.searchMovie();
  },
};
</script>

<style scoped>
.keyword-title h2 {
  font-weight: bold;
  margin-bottom: 10px;
  padding-bottom: 10px;
  position: relative;
  color: #173b6c;
}
.keyword-title h2::after {
  content: "";
  position: absolute;
  display: block;
  width: 100%;
  height: 3px;
  background: #068096;
  bottom: 0;
  left: 0;
}

</style>