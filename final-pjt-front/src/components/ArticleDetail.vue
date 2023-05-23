<template>
  <div>
    <div class="fullbox">
      <div id="banner">
        <img src="@/assets/banner.png">
      </div>
      <div class="articledetail">
        <div class="articlein">
          <div>
            <h3>{{ article?.title }}</h3>

            <div class="d-flex justify-content-between">
              <div class="userbox container">
                <div class="row">
                  <div class="row row-cols-auto">
                    <div class="col imgnick">
                      <img v-if="imgInfo" class="img-info" :src=imgInfo>
                      <span @click="goUser">{{ article?.username }}</span>
                    </div>
                    <p class="col align-middle">{{ article?.created_at.replace('T', ' ').slice(0, 16) }}</p>
                    <p class="col align-middle comt">댓글</p>
                    <p class="comlen">{{ commentList.length }}</p>
                  </div>
                </div>
              </div>
              <div class="buttons d-flex col-2 justify-content-end align-items-center">
                <p class="btn1" v-if="compareUser" @click="updateArticle">수정</p>
                <p>|</p>
                <p class="btn2" v-if="compareUser" @click="deleteArticle">삭제</p>
              </div>
            </div>

            <div class="contentbox">
              <p>{{ article?.content }}</p>
            </div>


            <hr>
          </div>
          <div>
            <div v-if="commentList">
              <p>댓글({{ commentList.length }})</p>
              <ArticleDetailComment v-for="comment in commentList" :key="comment.id" :comment="comment"
                @comment-deleted="getArticleDetail" />
            </div>
            <form @submit.prevent="createComment">
              <input id="commentbox" type="text" v-model="content">
              <div class="d-flex justify-content-end">
              <button id="submit">댓글쓰기</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleDetailComment from '@/components/ArticleDetailComment.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  components: {
    ArticleDetailComment
  },
  data() {
    return {
      article: null,
      commentList: null,
      content: null,
      imgInfo: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  computed: {
    compareUser() {
      if (this.article.username === this.$store.state.username) {
        return true
      }
      else {
        return false
      }
    }
  },
  methods: {
    goUser() {
      this.$router.push(`/profile/detail/${this.article.username}`)
    },
    getUserProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/about/${this.article.username}/profile/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.imgInfo = `http://127.0.0.1:8000` + res.data.profileimg
        })
    },
    deleteArticle() {
      axios({
        method: 'DELETE',
        url: `${API_URL}/articles/${this.article.id}/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.$router.push({ path: '/community/list' })
        })
    },
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.$route.params.id}/`,
      })
        .then((res) => {
          console.log(res.data)
          this.article = res.data
          this.commentList = res.data.comment_set
          this.getUserProfile()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/articles/${this.$route.params.id}/comments/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.getArticleDetail()
          this.content = null
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateArticle() {
      this.$router.push({
        name: 'ArticleCreate',
        params: { article: this.article }
      });
    }
  }

} 
</script>

<style scoped>
.fullbox {
  margin-bottom: 40px;
}


#banner {
  width: 100%;
}

#banner img {
  width: 100%;
  height: auto;
}

.articledetail {
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 5%;
  border: solid 1px rgb(187, 187, 187);
}

.articlein {
  margin: 5%;
}

.img-info {
  border-radius: 50%;
  height: 32px;
  width: 32px;
  margin-right: 10px;
}

.imgnick {
  padding: 0px;
  margin-right: 10px;
}

.comt {
  padding-right: 0px;
}

.comlen {
  color: rgb(70, 70, 109);
}

.userbox {
  margin-top: 20px;
  margin-bottom: 30px;
}

.userbox p {
  margin-bottom: 0px;
  display: flex;
  align-items: center;
}

.btn1 {
  margin-right: 5px;
}

.btn2 {
  margin-left: 5px;
}

.btn1:hover {
  text-decoration: underline;
  cursor: pointer;
}

.btn2:hover {
  text-decoration: underline;
  cursor: pointer;
}
.contentbox {
  margin-bottom: 30px;
}

#commentbox {
  position: relative;
  width: 100%;
  height: 89px;
  border: solid 1px rgb(187, 187, 187);
}


#submit {
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
}

#submit:hover {
  color: white;
  background-position: 99% 50%;
}
</style>