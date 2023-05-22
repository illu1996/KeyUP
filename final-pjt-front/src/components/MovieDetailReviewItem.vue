<template>
  <div class="row ms-3">
    <div class="col-7 d-flex mt-1">
    <a href="#"><h5 @click="goUser">{{ review.username }}</h5></a> : <p v-if="!editing">{{ review.content }}</p>
    </div>
    <div class="col-2">
      <button class='btn btn-primary' v-if="compareUser" @click="editing = true, compared = true" v-show="!compared">수정</button>
      <button class='btn btn-danger ms-1' v-if="compareUser" @click="deleteReview" v-show="!compared">삭제</button>
    </div>
    <div class="d-flex my-1">

    <input class="col-6" type="text" v-model="editContent" v-if="editing">
  <button class='offset-1 btn btn-danger' v-if="editing" @click="changeEditing">취소</button>
  <button class='btn btn-primary ms-1' v-if="editing" @click="updateReview">완료</button>

</div>
  </div>
</template>

<script>
import axios from 'axios';
const MY_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailReviewItem',
  props: {
    review: Object,
  },
  data() {
    return {
      compared: false,
      editing: false,
      editContent: '',
    };
  },
  computed: {
    compareUser() {
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
        method: 'DELETE',
        url: `${MY_URL}/movies/reviews/${this.review.id}/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
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

<style scoped>
a {
  text-decoration: none;
  cursor: grab;
}
a:link{
  color: royalblue;
}
a:hover {color:black;}
</style>