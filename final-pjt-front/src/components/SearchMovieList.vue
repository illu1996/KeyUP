<template>
    <div @click="changeMovie" class="movieCard" @mouseover="showDetails = true" @mouseout="showDetails = false">
    <img :src="getImage" class="card-img-top" alt="" style="width: 100%; height: 100%;">
    <div class="card-overlay" :class="{ 'show-details': showDetails }">
      <h5 class="card-title"><b>{{ movie.title }}</b></h5>
      <h6>평점 {{ movie.vote_average }}</h6>
      <p class="card-text">{{ truncateOverview }}</p>
    </div>
  </div>

</template>

<script>

// const MY_URL = 'http://127.0.0.1:8000'
export default {
  name: 'SearchMovieList',
  props: {
    movie: Object
  },
  data(){
    return{
      showDetails: false,
      // bgImg :`https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    }
  },
  computed:{
    getImage(){
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
    truncateOverview() {
      if (this.movie.overview.length > 40) {
        return this.movie.overview.slice(0, 40) + '...';
      } else {
        return this.movie.overview;
      }
    }
  },
  methods: {

changeMovie() {
  const movieinfo = this.movie
  this.$store.dispatch('changeMovie', movieinfo)
  this.$router.push({ name: 'MovieDetail' })
},
},
created() {
}
}
</script>

<style scoped>
.bg{
  object-fit: none; 
  background-position: center;
  /* background-size: cover; */
  background-repeat: none;
  width: 100%;
  height: 200vh;
}

</style>