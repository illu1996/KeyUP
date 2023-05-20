<template>
  <div>
    <p @click="goUser">작성자: {{ review.username }}</p>
    <p v-if="!editing">{{ review.content }}</p>
    <input type="text" v-model="editContent" v-if="editing">
    <button v-if="!editing" @click="editing = true">수정</button>
    <button v-else @click="updateReview">수정 완료</button>
    <button @click="deleteReview">삭제</button>
  </div>
</template>

<script>
import axios from 'axios';
const MY_URL = 'http://127.0.0.1:8000'

export default {
  name :'MovieDetailReviewItem',
  props : {
    review : Object,
  },
  data() {
    return {
      editing: false,
      editContent: '',
    };
  },
  methods: {
    deleteReview() {
      axios({
        method:'DELETE',
        url : `${MY_URL}/movies/reviews/${this.review.id}/`,
        headers : {
          "Authorization" : `Token ${this.$store.state.token}`,
        },
      })
      .then((res)=>{
        console.log(res.data)
        this.$emit('review-deleted')
      })
    },
    updateReview() {
      axios({
        method: 'PUT',
        url: `${MY_URL}/movies/reviews/${this.review.id}/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`,
        },
        data: {
          content: this.editContent,
        },
      })
        .then((res) => {
          console.log(res.data);
          this.editing = false;
          this.$emit('review-updated');
        });
      },
    goUser() {
    this.$router.push(`/profile/detail/${this.review.username}`)
    }
  },
  created() {
    this.editContent = this.review.content;
  },
}
</script>

<style>

</style>