<template>
  <div>
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
  }
}
</script>

<style>

</style>