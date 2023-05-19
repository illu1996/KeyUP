<template>
  <div>
    디테일 페이지
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성자 : {{ article?.username }}</p>

    <p>작성시간 : {{ article?.created_at.replace('T',' ').slice(0,16) }} </p>
    <p>수정시간 : {{ article?.created_at.replace('T',' ').slice(0,16) }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article:null,

    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail(){
      axios({
        method:'get',
        url:`${API_URL}/articles/${this.$route.params.id}/`,
      })
      .then((res)=>{
        console.log(res)
        this.article = res.data

      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }

} 
</script>

<style></style>