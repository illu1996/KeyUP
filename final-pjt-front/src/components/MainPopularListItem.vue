<template>
  <div @click="changeMovie" class="movieCard" @mouseover="showDetails = true" @mouseout="showDetails = false">
    <img :src="getImage" class="card-img-top" alt="NONONO">
    <div class="card-overlay" :class="{ 'show-details': showDetails }">
      <h5 class="card-title">{{ movie.title }}</h5>
      <h6>평점 {{ movie.vote_average }}</h6>
      <p class="card-text">{{ truncateOverview }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name:'MainPopularListItem',
  props : {
    movie : Object,
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

<style scoped>
.movieCard {
  position: relative;
  display: inline-block;
}

.card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.show-details {
  opacity: 1;
}

.card-overlay h5,
.card-overlay h6,
.card-overlay p {
  margin: 0;
  padding: 0;
  color: white;
  margin-left: 10px;
  margin-right: 10px;
  margin-top: 5px;
}

.card-overlay h6{
  opacity: 0.8;
}
</style>