<template>
  <div>
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
  }
}
</script>

<style>

</style>