<template>
  <div class="">
    <div class="row">
      <div class="col d-flex row-cols-auto">
        <img class="col me-2 imginfo" v-if="imgInfo" :src="imgInfo" alt="">
        <img class="col imginfo" v-else src="@/assets/user.png" alt="">
        <p @click="goUser" class="col name align-middle comuser">{{ review.username }}</p>
      </div>

      <div class="col d-flex justify-content-end" id="updatedelete">
        <span class='btnon' v-if="compareUser" @click="editing = true, compared = true" v-show="!compared">수정|</span>

        <span class='btnon' v-if="compareUser" @click="deleteReview" v-show="!compared">삭제</span>
      </div>

      <p id="review">{{ review.content }}</p>
    </div>

    <div class="inputbox">
      <textarea class="updateinput col" type="text" v-model="editContent" v-if="editing"></textarea>
      <div class="d-flex justify-content-end align-items-center">
        <button class='submit' v-if="editing" @click="updateReview">완료</button>
        <button class='submit' v-if="editing" @click="changeEditing">취소</button>
      </div>
    </div>
    <hr>
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
      editContent: null,
      imgInfo: null,
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
      const editContent = this.editContent
      if (!editContent) {
        alert('내용을 입력해주세요')
        return
      }
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
    },
    getUserProfile() {
      axios({
        method: 'get',
        url: `${MY_URL}/accounts/about/${this.review.username}/profile/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          if (res.data.profileimg) {
            this.imgInfo = `http://127.0.0.1:8000` + res.data.profileimg           
          }
        })
    },
  },
  created() {
    this.editContent = this.review.content;
    this.getUserProfile()
  },
}
</script>

<style scoped>

.inputbox {
  margin-left: 3.5%;
}

#updatedelete {
  margin-right: 2%;
}
.imginfo {
  margin-right: 7px;
}
.comuser:hover {
  text-decoration: underline;
  cursor: pointer;
}

.comuser {
  font-weight: 700;
}

#updatedelete span {
  margin-top: auto;
  margin-bottom: auto;
}


.btnon:hover {
  text-decoration: underline;
  cursor: pointer;
}

.updateinput {
  width: 100%;
  height: 89px;
  border: solid 1px rgb(187, 187, 187);
  /* margin-right: auto; */
  outline: none;
}

.submit {
  font-size: 12px !important;
  /* margin-top: 20px; */
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
  margin-top: 3px;
}

.updateinput {
  width: 100%;
  height: 89px;
  border: solid 1px rgb(187, 187, 187);
  margin-right: auto;
}


#review {
  margin-left: 4%;
  margin-top: 5px;
}

img {
  border-radius: 50%;
  height: 32px;
  width: 32px;
  margin-left: 10px;
  margin-top: 10px;
  padding-right: 0px;
  padding-left: 0px;
}

.name {
  margin-top: 10px;
}

hr {
  /* margin-top: 5px; */
  margin: 0;
}

a {
  text-decoration: none;
  cursor: grab;
}

a:link {
  color: royalblue;
}

a:hover {
  color: black;
}
</style>