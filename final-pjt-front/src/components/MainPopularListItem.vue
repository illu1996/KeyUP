<template>
  <div>
    <img :src="getImage" class="card-img-top" alt="NONONO">
    <h5 class="card-title">{{ movie.title }}</h5>
  </div>
</template>

<script>
export default {
  name:'MainPopularListItem',
  props : {
    movie : Object,
  },
  computed: {
    getImage() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
  }
}
</script>

<style>

</style>