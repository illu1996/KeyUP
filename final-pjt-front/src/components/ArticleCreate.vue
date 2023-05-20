<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="handleSubmit">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
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
        this.$router.push({name: 'CommunityView'})
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
        this.$router.push({name: 'CommunityView'})
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

<style>

</style>