<template>
<div>
    <p @click="goUser">작성자: {{ review.username }}</p>
    <p v-if="!editing">{{ review.content }}</p>
    <input type="text" v-model="editContent" v-if="editing">
    <button v-if="compareUser" @click="editing = true, compared =true" v-show="!compared">수정</button>
    <div v-if="editing">
      <button @click="changeEditing">취소</button>
      <button @click="updateReview">수정 완료</button>
    </div>
    <button v-if="compareUser" @click="deleteReview" v-show="!compared">삭제</button>
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
      compared: false,
      editing: false,
      editContent: '',
    };
  },
  computed: {
    compareUser(){
      if (this.review.username === this.$store.state.username) {
        return true
      }
      else {
        return false
      }
    }

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
          this.compared = !this.compared
                
          this.$emit('review-updated');
        });
      },
    goUser() {
    this.$router.push(`/profile/detail/${this.review.username}`)
    },
    changeEditing() {
      this.editing = !this.editing
      this.compared = !this.compared

    }
  },
  created() {
    this.editContent = this.review.content;
  },
}
</script>

<style>

</style>