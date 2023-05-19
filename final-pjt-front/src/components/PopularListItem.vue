<template>
  <div @click="changeMovie">
    <img :src="getImage" class="card-img-top" alt="NONONO">
    <h5 class="card-title">{{ movie.title }}</h5>
  </div>
</template>

<script>
export default {
  name:'PopularListItem',
  props : {
    movie : Object,
  },
  computed: {
    getImage() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
  },
  methods: {
    changeMovie() {
      const movieinfo = this.movie
      this.$store.dispatch('changeMovie', movieinfo)
      this.$router.push({name:'MovieDetail'})
    }
  },
}
</script>

<style>

</style>