<template>
  <div>
    <div class="container articlelist">
      <div class="art-parent">
        <h6 class="art-ani">게시글 수 <span><b>{{ articlelen }}</b></span></h6>
      </div>
      <div class="container text-center">
        <div class="row align-items-center">
          <p class="col-1">글번호</p>
          <p class="col-8">제목</p>
          <p class="col-1">작성자</p>
          <p class="col-2">작성일</p>
        </div>
      </div>
      <div>
        <div class="container">
          <hr class="hihi">
          <ArticleListItem v-for="article in articleList" :key="article.id" :article="article" />
        </div>
      </div>
      <div class="d-flex justify-content-end">
        <button @click="createPage">글쓰기</button>
      </div>
    </div>
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
      articleList: []
    }
  },
  computed: {
    articlelen() {
      return this.articleList.length
    }
  },
  methods: {
    articles() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.articleList = res.data

        })
        .catch((err) => {
          console.log(err)
        })
    },
    createPage() {
      this.$router.push('/community/create');
    }
  },
  created() {
    this.articles()
  }
}
</script>

<style scoped>

.art-ani{

  display: inline-block;
  padding-bottom: 4px;
  letter-spacing: 1px;
  border-bottom: 3px solid #149ddd;

}

@media screen and (min-width: 768px) {
  .title-container {
    margin-left: 10%;
  }
}

@media screen and (min-width: 720px) {
  .title-container {
    margin-left: 9%;
  }
}
.articlelist {
  /* position: relative; */
  /* border: solid 1px rgb(221, 221, 221); */
  margin-left: 10%;
  margin-right: 10%;
  margin-bottom: 70px;
  margin-top: 0%;
  border-left: none;
  border-right: none;
}

.hihi {
  margin-top: 2px;
}

.container div p {
  margin-bottom: 3px;
  margin-top: 3px;
}

h6 {
  margin-top: 4%;

  padding-bottom: 20px;
  margin-bottom: 20px;
}

button {
  font-size: 13px !important;
  margin-top: 5px;
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


button:hover {
  color: white;
  background-position: 99% 50%;
}
</style>
