<template>
  <div>
    <p>닉네임 : {{ user?.nickname }}</p>
    <p>사진... : <img :src=imgInfo alt=""></p>
    <p>소개말 : {{ user?.introduce }}</p>
    <p>좋아요 한 영화</p>
    <div v-for="movie in movielist" :key="movie.id">
      <p>{{ movie.title }}</p>
      <img :src="getImageUrl(movie.poster_path)" alt="">
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProfileDetail',
  data() {
    return {
      movielist :[],
      user : this.$store.state.userInfo,
      imgInfo : null,
    }
  },
  beforeRouteUpdate(to, from, next)  {
    next()
  },
  computed: {
    
  },
  watch: {
    user: {
      immediate: true,
      handler(newValue) {
        if (newValue && newValue.like_movies) {
          this.movielist = []; // 기존 영화 목록 초기화
          this.getMovies();
        }
      }
    }
  },
  methods: {
    getImageUrl(posterPath) {
      return `https://image.tmdb.org/t/p/original/${posterPath}`;
    },
    getMovies() {
      const movies = this.user?.like_movies
      for (let movie of movies) {
        axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/movie/${movie}?language=ko-kr`,
          headers: {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
          }
        })
        .then((res)=>{
          this.movielist.push(res.data)
          this.imgInfo = `http://127.0.0.1:8000/` + this.$store.state.userInfo.profileimg
        })
      }
    },
  },
}
</script>

<style></style>