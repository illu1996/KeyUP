<template>
  <div>
    <div class="card" style="width: 18rem;" @mouseover="showDetails = true" @mouseout="showDetails = false">
      <img :src="getImage" class="card-img-top" alt="NONONO">
      <div class="card-overlay" :class="{ 'show-details': showDetails }">
        <h5 class="card-title">{{ movie.title }}</h5>
        <h6>{{ movie.vote_average }}</h6>
        <p class="card-text">{{ truncateOverview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'LatestListItem',
  props: {
    movie: Object,
  },
  data() {
    return {
      showDetails: false
    };
  },
  computed: {
    getImage() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
    truncateOverview() {
      if (this.movie.overview.length > 30) {
        return this.movie.overview.slice(0, 30) + '...';
      } else {
        return this.movie.overview;
      }
    }
  }
}
</script>

<style>

</style>


