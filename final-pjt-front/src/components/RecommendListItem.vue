<template>
  <div>
    <p>{{movie}}</p>
    <img :src=poster_path alt="">
  </div>
</template>

<script>
export default {
  name:'RecommendListItem',
  props:{
    movie:Object,
  },
  data(){
    return {
      poster_path:null
    }
  },
    methods: {
    getImage() {
      this.poster_path = `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
  },
  created(){
    this.getImage()
}
}
</script>

<style>

</style>