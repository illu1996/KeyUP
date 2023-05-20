<template>
  <div>
    <h3>리뷰입니당 :)</h3>
    <div>
      <MovieDetailReviewItem v-for="review in reviews" :key="review.id" :review="review"
      @review-deleted="getReviews" @review-updated="getReviews"/>
    </div>
    <div>
      <label for="content">리뷰를 작성해주세요</label>
      <input type="text" id="content" v-model="content">
      <button @click="addReview">작성하기</button>
    </div>
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
      reviews: [],
      content : null,
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

    addReview() {
      const content = this.content
      axios({
        method:'post',
        url : `${MY_URL}/movies/${this.movie_id}/reviews/`,
        data : {
          content
        },
        headers : {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then(()=>{
        this.getReviews()
        this.content = null
      })
      .catch((err)=>{
        console.log(err)
      })
    },
  },
  created() {
    this.getReviews()
  },
}
</script>

<style>

</style>