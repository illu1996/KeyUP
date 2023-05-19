<template>
  <div>
    <h3>리뷰입니당 :)</h3>
    <MovieDetailReviewItem v-for="review in reviews" :key="review.id" :review="review"/>
  </div>
</template>

<script>
const MY_URL = 'http://127.0.0.1:8000'
import axios from 'axios';
import MovieDetailReviewItem from '@/components/MovieDetailReviewItem.vue'


export default {
  name : 'MovieDetailReview',
  props: {
    movie_id : Number,
  },
  components: {
    MovieDetailReviewItem
  },
  data() {
    return {
      reviews: []
    }
  },
  methods: {
    getReviews() {
      axios({
        method :'get',
        url : `${MY_URL}/movies/${this.movie_id}/reviews/`,
      })
      .then((res)=>{
        this.reviews = res.data
      })
      .catch((err)=>{
        if (err.response && err.response.status === 404) {
          this.reviews = [];
        } else {
          console.error('Error:', err)
        }})
    },
  },
  created() {
    this.getReviews()
  }
}
</script>

<style>

</style>