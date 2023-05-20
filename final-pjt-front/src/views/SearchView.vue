<template>
  <div>
    <div>
      관련된 영화
    </div>
    {{keyword}}와(과) 관련된 영화 제목은 총 {{ movieList.length }}개 입니다.

    <div v-if="movieList.length > 0">
      <SearchMovieList v-for="movie in movieList" :key="movie.id" :movie="movie" />
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

<style></style>