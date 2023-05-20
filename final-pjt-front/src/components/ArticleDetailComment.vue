<template>
  <div>
    <p>작성자 : {{ comment.username }}</p>
    <p>대충 내용 : {{ comment.content }}</p>
    <!-- <button v-if="compareUser" @click="updateArticle">수정</button> -->
    <button v-if="compareUser" @click="updateComment" v-show="!compared">수정</button>
    <div v-if="updateform">
      <input type="text" v-model="editContent">
      <button @click="updateReview">수정 완료</button>
      <button @click="changeEditing">취소</button>
    </div>
    <button v-if="compareUser" @click="deleteComment" v-show="!compared">삭제</button>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailComment',
  props: {
    comment: Object,
  },
  data() {
    return {
      compared: false,
      content: null,
      updateform: false,
      editContent: this.comment.content,
    }
  },
  computed: {
    compareUser() {
      if (this.comment.username === this.$store.state.username) {
        return true
      }
      else {
        return false
      }
    },
  },
  methods: {

    updateComment() {
      this.updateform = true
      this.compared = !this.compared
    },
    deleteComment() {
      console.log(this.comment)
      axios({
        method: 'DELETE',
        url: `${API_URL}/articles/comments/${this.comment.id}/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.$emit('comment-deleted');
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateReview() {
      axios({
        method: 'PUT',
        url: `${API_URL}/articles/comments/${this.comment.id}/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`,
        },
        data: {
          content: this.editContent,
        },
      })
        .then((res) => {
          console.log(res.data);
          this.updateform = false;
          this.compared = !this.compared
          this.$emit('comment-deleted');
        });
    },
    changeEditing() {
      this.updateform = !this.updateform
      this.compared = !this.compared
    }
  },
}
</script>

<style></style>