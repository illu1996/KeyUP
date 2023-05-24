<template>
  <div class="container">
    <div class="row">
      <MovieDetailReviewItem v-for="review in reviews" :key="review.id" :review="review" @review-deleted="getReviews"
        @review-updated="getReviews" />
    </div>
      <div class="row">
        <label for="exampleFormControlTextarea1" class="form-label"></label>
        <textarea v-model="content" class="updateinput" id="exampleFormControlTextarea1" rows="2"></textarea>
        </div>
        <div class="d-flex justify-content-end align-items-center">
        <button @click="addReview" type="button" class="submit">작성하기</button>
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
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
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

<style scoped>
.updateinput {
  width: 97%;
  height: 89px;
  border: solid 1px rgb(187, 187, 187);
  margin-top:10px; 
  margin-left:20px;
  margin-right: 20px;
  outline: none;
}

.submit {
  font-size: 12px !important;
  margin-top: 20px;
  margin-right: 0%;
  margin-bottom: 2%;
  background-color: rgb(138, 138, 138);
  color: white;
  display: inline-block;
  padding: 0.8em 1.6em;
  width: 100px;
  border-radius: 0;
  color: rgb(24, 24, 53);
  font-weight: bold;
  font-size: 0.678rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  text-decoration: none;
  background: linear-gradient(to right, rgba(178, 135, 111, 0) 25%, rgba(65, 73, 129, 0.8) 75%);
  background-position: 1% 50%;
  background-size: 400% 300%;
  border: 1px solid rgb(138, 138, 138);
  transition: all 0.3s;
  opacity: 0.7;
  margin-left: 5px;
}

.submit:hover {
  color: white;
  background-position: 99% 50%;
}
</style>
