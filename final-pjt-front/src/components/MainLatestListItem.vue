<template>

    <div href="javascript:void(0)" class="overlay-img">
      <img :src="getImage" alt="NONONO" style="width:100px; height:100px;">
      <div class="overlay"></div>
      <div class="des">
        <h1 class="title" id="card1">{{ movie.title }} {{ movie.vote_average }}</h1>
        <h6 class="subtitle" id="card1-text"> {{ movie.overview }}</h6>
      </div>
    </div>

</template>

<script>
export default {
  name: 'MainLatestListItem',
  props: {
    movie: Object,
  },
  computed: {
    getImage() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    }
  }

}
</script>

<style scoped></style>