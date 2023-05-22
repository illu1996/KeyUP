<template>
  <div class="container">
    <div class="row">
      <MovieDetailReviewItem v-for="review in reviews" :key="review.id" :review="review" @review-deleted="getReviews"
        @review-updated="getReviews" />
    </div>
    <div class="row justify-content-center align-items-center">
      <div class="mb-3 col-8">
        <label for="exampleFormControlTextarea1" class="form-label"></label>
        <textarea v-model="content" class=" form-control" id="exampleFormControlTextarea1" rows="2"></textarea>
        </div>
        <div class="col-4">
        <button @click="addReview" type="button" class="btn btn-dark">완료</button>
      </div>

    </div>
  </div>
</template>

<script>
const MY_URL = 'http://127.0.0.1:8000'
import axios from 'axios';
import MovieDetailReviewItem from '@/components/MovieDetailReviewItem.vue'


export default {
  name: 'MovieDetailReview',
  props: {
    movie_id: Number,
  },
  components: {
    MovieDetailReviewItem
  },
  data() {
    return {
      reviews: [],
      content: null,
    }
  },
  methods: {
    getReviews() {
      axios({
        method: 'get',
        url: `${MY_URL}/movies/${this.movie_id}/reviews/`,
      })
        .then((res) => {
          this.reviews = res.data
        })
        .catch((err) => {
          if (err.response && err.response.status === 404) {
            this.reviews = [];
          } else {
            console.error('Error:', err)
          }
        })
    },

    addReview() {
      const content = this.content
      axios({
        method: 'post',
        url: `${MY_URL}/movies/${this.movie_id}/reviews/`,
        data: {
          content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.getReviews()
          this.content = null
        })
        .catch((err) => {
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
