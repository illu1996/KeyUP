<template>
  <div>
    <div class="hero">
      <div class="hero-slide">
        <!-- <div class="img overlay" style="background-image: url('@/asset/메인2.jpg')"></div> -->
      </div>

      <div class="container">
        <div class="row justify-content-center align-items-center">
          <div class="col text-center">
            <h1 class="heading" data-aos="fade-up">
              키워드 검색
            </h1>
            <form @submit.prevent="keywordExtract" class="narrow-w form-search d-flex align-items-stretch mb-3"
              data-aos="fade-up">
              <input @enter="keywordExtract" v-model="inputbox" type="text" class="form-control px-4" placeholder="키워드를 입력하세용용용" />
              <button type="submit" class="btn btn-primary">Search</button>
            </form>

            <div id="randomkey" class="col d-flex align-items-center">
              <span><strong>추천 키워드 :</strong></span>
              <button class="btn col border" v-for="randomkeyword in randomKeywordList" :key="randomkeyword.id"
                @click="getkeywordMovie(randomkeyword.id)">
                {{ randomkeyword.translated }}</button>
            </div>
          </div>
          <div class="text-center row">
            <p>검색된 키워드</p>
            <!-- <p v-if="!searchkeywordList">관련된 검색어가 없습니다.</p> -->
            <button class='btn border col-1' v-for="searchkeyword in searchkeywordList" :key="searchkeyword.id" @click="getkeywordMovie(searchkeyword.id)">
              {{ searchkeyword.translated }}</button>
          </div>
          <div class='row mt-3' v-if="this.keywordMovieList">
            <RecommendListItem class='col-4 p-1' v-for="movie in keywordMovieList" :key="movie.id" :movie="movie" />
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import RecommendListItem from './RecommendListItem.vue'
import axios from 'axios';
import _ from 'lodash'
const MY_URL = 'http://127.0.0.1:8000'

export default {
  name: 'RecommendList',
  components: {
    RecommendListItem,
  },
  data() {
    return {
      similarList: [],
      keywordList: [],
      randomKeywordList: [],
      showSwitch: false,
      inputbox: null,
      searchkeywordList: [],
      keywordMovieList: [],
      poster_path: null
    }
  },
  methods: {
    randomKeyword() {
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
    keywordExtract() {
      this.showSwitch = !this.showSwitch
      this.keywordMovieList = []
      this.searchkeywordList = []
      for (let keyword of this.keywordList) {
        if (keyword.translated.includes(`${this.inputbox}`)) {
          this.searchkeywordList.push(keyword)
        }
      }
    },
    getkeywordMovie(key_id) {
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

<style></style>