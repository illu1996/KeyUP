<template>
  <div @click="changeMovie">
    <h1>{{genreMovie.title}}</h1>
    <hr>
    <h6>{{genreMovie.overview}}</h6>

  </div>
</template>

<script>
export default {
  name:'GenreListItem',
  props:{
    genreMovie:Object
  },
  methods: {
    changeMovie() {
      const movieinfo = this.genreMovie
      this.$store.dispatch('changeMovie', movieinfo)
      this.$router.push({name:'MovieDetail'})
    }
  }
}
</script>

<style>

</style>