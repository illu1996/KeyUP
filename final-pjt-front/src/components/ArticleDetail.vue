<template>
  <div>
    디테일 페이지
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p @click="goUser" >작성자 : {{ article?.username }}</p>

    <p>작성시간 : {{ article?.created_at.replace('T',' ').slice(0,16) }} </p>
    <p>수정시간 : {{ article?.created_at.replace('T',' ').slice(0,16) }}</p>
    <button v-if="compareUser" @click="updateArticle">수정</button>
    <button v-if="compareUser" @click="deleteArticle">삭제</button>
    <hr>

    <div v-if="commentList">
      <p>댓글리스트 :)</p>
      <ArticleDetailComment v-for="comment in commentList" :key="comment.id"
      :comment="comment" @comment-deleted="getArticleDetail"/>
    </div>
    <form @submit.prevent="createComment">
      <input type="text" v-model="content">
      <button>입력하기</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleDetailComment from '@/components/ArticleDetailComment.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  components:{
    ArticleDetailComment
  },
  data() {
    return {
      article:null,
      commentList : null,
      content: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  computed:{
    compareUser(){
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
    deleteArticle() {
      axios({
        method:'DELETE',
        url : `${API_URL}/articles/${this.article.id}/`,
        headers : {
          "Authorization" : `Token ${this.$store.state.token}`,
        },
      })
      .then((res)=>{
        console.log(res.data)
        this.$router.push({path:'/community/list'})
      })
    },
    getArticleDetail(){
      axios({
        method:'get',
        url:`${API_URL}/articles/${this.$route.params.id}/`,
      })
      .then((res)=>{
        console.log(res.data)
        this.article = res.data
        this.commentList = res.data.comment_set
      })
      .catch((err)=>{
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
        headers:{
          Authorization : `Token ${ this.$store.state.token }`
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
        params: { article: this.article}
      });
    }
  }

} 
</script>

<style></style>