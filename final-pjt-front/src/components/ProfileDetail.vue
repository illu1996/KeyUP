<template>
  <div>
    <div v-if="userInfo && this.$store.state.username != userInfo.username">

      <button v-if="!followers.includes(this.$store.state.username)" @click="follow">팔로우</button>
      <button v-else @click="follow">팔로우 취소</button>

    </div>
    <p>팔로워 : {{ follower }} | 팔로잉 : {{ following }}</p>
    <p>닉네임 : {{ userInfo?.nickname }}</p>
    <p>사진 : <img :src=imgInfo alt=""></p>
    <p>소개말 : {{ userInfo?.introduce }}</p>
    <p>좋아요 한 영화</p>
    <div v-for="(movie, index) in movielist" :key="index" @click="changeMovie(movie)">
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
    changeMovie(movie) {
      const movieinfo = movie
      this.$store.dispatch('changeMovie', movieinfo)
      this.$router.push({name:'MovieDetail'})
    },
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
          const movieData = res.data;
          if (this.movielist.some((movie) => movie.id === movieData.id)) {
            return;
          }
          this.movielist.push(res.data)
          if (this.userInfo.profileimg) {
            this.imgInfo = `http://127.0.0.1:8000/` + this.userInfo.profileimg
          }
        })
      }
    },

    
    infoOfuser() {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/accounts/about/${this.$route.params.username}/profile/`
      })
      .then((res)=>{
        this.userInfo = res.data
        this.getMovies()
        this.creatfollow()
      })
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
        this.followers = res.data.person.followers
      })
    },

    creatfollow() {
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/about/${this.userInfo.id}/follow/`,
      })
      .then((res)=>{
        console.log(res.data.person.followers)
        this.follower = res.data.followers_count
        this.following = res.data.followings_count
        this.followers = res.data.person.followers
      })
    },


  },
  created() {
    this.infoOfuser()
  }
}
</script>

<style></style>
