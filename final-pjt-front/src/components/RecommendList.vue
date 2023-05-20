<template>
  <div>
    <form @submit.prevent="keywordExtract">
      <input type="text" value="" v-model="inputbox">
      <button>검색</button>
    </form>
    <button v-for="randomkeyword in randomKeywordList" 
    :key="randomkeyword.id" @click="getkeywordMovie(randomkeyword.id)">
    {{randomkeyword.translated}}</button>
    <div>
      <p v-for="searchkeyword in searchkeywordList" 
      :key="searchkeyword.id" @click="getkeywordMovie(searchkeyword.id)">
      {{ searchkeyword.translated }}</p>
    </div>
    <div v-if="this.keywordMovieList">
      <RecommendListItem v-for="movie in keywordMovieList" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>

<script>
import RecommendListItem from './RecommendListItem.vue'
import axios from 'axios';
import _ from 'lodash'
const MY_URL = 'http://127.0.0.1:8000'

export default {  
  name :'RecommendList',
  components:{
    RecommendListItem,
  },
  data() {  
    return {
      similarList:[],
      keywordList: [],
      randomKeywordList :[],
      showSwitch : false,
      inputbox:null,
      searchkeywordList :[],
      keywordMovieList:[],
      poster_path:null
    }
  },
  methods:{
    randomKeyword(){
      this.randomKeywordList = _.sampleSize(this.keywordList, 10)
    },
    getKeyNumber() {
      axios({
        method: "GET",
        url: `${MY_URL}/movies/keywords/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.keywordList = res.data
          this.randomKeyword()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    keywordExtract(){
      this.showSwitch = !this.showSwitch
      this.keywordMovieList =[]
      this.searchkeywordList =  []
      for (let keyword of this.keywordList){
        if (keyword.translated.includes(`${this.inputbox}`)){
          this.searchkeywordList.push(keyword)
        }
      }
    },
    getkeywordMovie(key_id){
      axios({
        method: "GET",
        url: `${MY_URL}/movies/keywords/${key_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.searchkeywordList = []
          this.keywordMovieList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.getKeyNumber()
  },

}
</script>

<style>

</style>