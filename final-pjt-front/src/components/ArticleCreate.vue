<template>
  <div class="createForm">
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="title"></label>
        <input type="text" id="title" v-model.trim="title" placeholder="제목을 입력하세요"><br>
      </div>
      <hr>
      <div>
        <label for="content"></label>
        <textarea id="content" cols="30" rows="10" v-model="content" placeholder="내용을 입력하세요"></textarea><br>
      </div>
      <div class="d-flex justify-content-end">
        <input type="submit" id="submit" value="작성하기">
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'ArticleCreate',
  data() {
    return {
      title: null,
      content: null,
      article : null,
    }
  },
  methods: {
    handleSubmit() {
      if (this.article) {
        this.updateArticle();
      } else {
        this.createArticle();
      }
    },
    createArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
        data: { title, content },
        headers:{
          Authorization : `Token ${ this.$store.state.token }`
        }
      })
      .then(() => {
        // console.log(res)
        this.$router.push({name: 'ArticleList'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/articles/${this.$route.params.article.id}/`,
        data: { title, content },
        headers:{
          Authorization : `Token ${ this.$store.state.token }`
        }
      })
      .then(() => {
        // console.log(res)
        this.$router.push({name: 'ArticleDetail', params: { id: this.$route.params.article.id }})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
    if (this.$route.params) {
      this.article = this.$route.params?.article
      this.title = this.$route.params.article?.title
      this.content = this.$route.params.article?.content
    }
  }
}
</script>

<style scoped>
.createForm {
  border: solid 1px rgb(221, 221, 221);
  margin-left: 10%;
  margin-right: 10%;
  margin-bottom: 70px;
  margin-top: 3%;
}

#title { 
  width: 90%;
  border: none;
  outline: none;
  border-bottom: solid 1px rgb(201, 201, 201);
  margin-left: 5%;
  margin-right: 5%;
  /* margin-bottom: 2%; */
  padding-top: 20px;
  /* padding-bottom: 2px; */
}

#content {
  width: 91%;
  margin-left: 5%;
  margin-right: 5%;
  border: none;
  outline: none;
  height: 400px;
}


#submit {
  font-size: 13px !important;
  margin-top: 20px;
  margin-right: 5%;
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