<template>
  <div>
    {{ movie }}
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
      bgImg :`https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    }
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