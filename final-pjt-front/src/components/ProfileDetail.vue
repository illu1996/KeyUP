<template>
  <div>
    <div v-if="this.$store.state.username != userInfo.username">
      <button @click="follow">팔로우하기</button>
      <p>팔로워 : {{ follower }} | 팔로잉 : {{ following }}</p>
    </div>
    <p>닉네임 : {{ userInfo?.nickname }}</p>
    <p>사진... : <img :src=imgInfo alt=""></p>
    <p>소개말 : {{ userInfo?.introduce }}</p>
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
      userInfo : null,
      follower : null,
      following : null,
      userName : this.$route.params.username
    }
  },
  computed: {
  },
  watch: {
    $route(to) {
      this.userName = to.params.username;
      this.infoOfuser();
    },
    userInfo: {
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
      const movies = this.userInfo?.like_movies
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
          this.imgInfo = `http://127.0.0.1:8000/` + this.userInfo.profileimg
        })
      }
    },
    infoOfuser() {
      for (let info of this.$store.state.usersInfo) {
        if (info.username === this.$route.params.username) {
          this.userInfo = info
          break
        }
      }
    },
    follow() {
      axios({
          method: 'post',
          url: `http://127.0.0.1:8000/accounts/about/${this.userInfo.id}/follow/`,
          headers: {
            Authorization : `Token ${this.$store.state.token }`
          },
      })
      .then((res)=>{
        console.log(res.data)
        this.follower = res.data.followers_count
        this.following = res.data.followings_count
      })
    }
  },
  created() {
    this.infoOfuser()
  }
}
</script>

<style></style>