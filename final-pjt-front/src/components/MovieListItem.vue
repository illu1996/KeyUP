<template>
  <div @click="changeMovie">
    <h1>{{ randomMovie.title }}</h1>
    <hr>
    <p>{{ randomMovie.overview }}</p>
  </div>
</template>

<script>
export default {
  name:'MovieListItem',
  props:{
    randomMovie: Object
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