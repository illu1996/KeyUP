<template>
  <div>
    <div class="container idbox">
      <div class="row row-cols-auto" id="comment">
        <img v-if="imgInfo" class="col" :src=imgInfo>
        <img v-else src="@/assets/user.png" alt="">
        <p class="col align-middle">{{ comment.username }}</p>
        <p class="col align-middle">{{ createtime }}</p>
      </div>
    </div>

    <div>
      <div class="container">
        <div class="row" id="comment">
          <p class="col content">{{ comment.content }}</p>
          <div class="d-flex col-2 justify-content-end align-items-center">
            <p class="btnon" v-if="compareUser" @click="updateComment" v-show="!compared">수정</p>
            <p v-if="compareUser">&nbsp;|&nbsp;</p>
            <p class="btnon" v-if="compareUser" @click="deleteComment" v-show="!compared">삭제</p>
          </div>
        </div>
      </div>
      <div v-if="updateform">
        <input type="text" v-model="editContent" class="updateinput">
        <div class="d-flex justify-content-end">
          <button class="submit" @click="updateReview">수정하기</button>
          <button class="submit" @click="changeEditing">취소</button>
        </div>
      </div>
    </div>
    <br>
    <hr>
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
      imgInfo: null,
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
    createtime() {
      return this.comment.created_at.replace('T', ' ').slice(0, 16)
    }
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
    },
    getUserProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/about/${this.comment.username}/profile/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.imgInfo = `http://127.0.0.1:8000` + res.data.profileimg
        })
    },
  },
  created() {
    this.getUserProfile()
  }
}
</script>

<style scoped>
#comment p{
  font-size: 0.85em;
}
img {
  border-radius: 50%;
  height: 25px;
  width: 25px;
  /* margin-right: 10px; */
  padding-right: 0px;
  padding-left: 0px;
}

.row-cols-auto p {
  margin-bottom: 0px;
}

.idbox {
  margin-bottom: 10px;
}

.content {
  margin-left: 2.5%;
}

.updateinput {
  width: 100%;
  height: 89px;
  border: solid 1px rgb(187, 187, 187);
  margin-right: auto;
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

.btnon:hover {
  text-decoration: underline;
  cursor: pointer;
}
</style>