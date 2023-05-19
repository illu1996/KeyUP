<template>
  <div>
    <h1>글목록</h1>
    <ArticleListItem 
    v-for="article in articleList" :key="article.id" :article="article" />
  </div>
</template>

<script>
import axios from 'axios'
import ArticleListItem from './ArticleListItem.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  data() {
    return {
      articleList:[]
    }
  },
  methods: {
    articles() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers:{
          Authorization : `Token ${ this.$store.state.token }`
        }
      })
      .then((res) => {
        this.articleList = res.data

      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created(){
    this.articles()
  }
}
</script>

<style>

</style>
