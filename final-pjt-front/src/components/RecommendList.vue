<template>
  <div>
    <div class="hero">
      <div class="hero-slide">
        <div class="img overlay background" :style="`background-image: url(${require('@/assets/메인2.png')})`"></div>
      </div>

      <div class="container">
        <div class="row justify-content-center align-items-center">
          <div class="col text-center">
            <h1 class="heading -webkit-text-stroke-width: 3px;" data-aos="fade-up">
              키워드 검색
            </h1>
            <form @submit.prevent="keywordExtract" class="narrow-w form-search d-flex align-items-stretch mb-3"
              data-aos="fade-up">
              <input @enter="keywordExtract" v-model="inputbox" type="text" class="form-control px-4"
                placeholder="키워드를 입력하세용" />
              <button type="submit" class="btn btn-primary">Search</button>
            </form>

            <div id="randomkey" class="col d-flex align-items-center">
              <span><strong>추천 키워드 :</strong></span>
              <button class="btn col border" v-for="randomkeyword in randomKeywordList" :key="randomkeyword.id"
                @click="getkeywordMovie(randomkeyword.id)">
                <b>{{ randomkeyword.translated }}</b> </button>
            </div>

            <div class="text-center row">
              <b><h2> 검색된 키워드</h2></b>
              <p v-if="!keywordcount">관련된 검색어가 없습니다.</p>
              <button class='btn border col-1' v-for="searchkeyword in searchkeywordList" :key="searchkeyword.id"
                @click="getkeywordMovie(searchkeyword.id)">
                <b>{{ searchkeyword.translated }}</b></button>
            </div>
          </div>

        </div>
      </div>
      <div class="section">
      <div class="container">
        <div class="row mb-5 align-items-center">
          <div class="col-lg-6">
            <h2 class="font-weight-bold heading">
              검색된 영화
            </h2>
          </div>
    
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
      poster_path: null,
      keywordcount:null,
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
      this.keywordcount = this.searchkeywordList.length
      this.inputbox = null
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
          this.inputbox = null
          this.keywordcount = null

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
.text-center h1{
  /* -webkit-text-stroke: 2px black; */
}
.bg-image {
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

.bg-image.overlay {
  position: relative;
}

.bg-image.overlay:before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 1;

}

.bg-image>.container,
.bg-image .custom-box {
  position: relative;
  z-index: 2;
}

.background {
  opacity: 0.2;
  background-attachment: fixed;
}

img,
svg {
  vertical-align: middle;
}

.hero-slide {
  top: 0;
  position: absolute;
  left: 0;
  right: 0;
}

.hero-slide .img {
  height: 100%;
  min-height: 600px;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
}

.hero-slide .img.overlay {
  position: relative;
}

.hero-slide .img.overlay:before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 1;
  background: rgba(34, 34, 34, 0.2);
}

.hero {
  position: relative;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-color: rgba(200, 200, 200, 0.1);
  
}

.hero.overlay {
  position: relative;
}

.hero.overlay:before {
  /* background-color: rgba(255, 255, 255, 1); */
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 1;
}

.hero,
.hero>.container>.row {
  height: 50vh;
  min-height: 600px;
}

.hero.page-inner,
.hero.page-inner>.container>.row {
  height: 100%;
  min-height: 300px;
}

.hero>.container {
  position: relative;
  z-index: 2;
}

.hero .heading {
  /* color: #fff; */
  font-size: clamp(3rem, 2.5vw, 2.5rem);
  margin-bottom: 30px;
  font-weight: 600;
}

.hero .lead {
  color: #fff;
  font-size: 14px;
  margin-bottom: 30px;
}

.hero .narrow-w {
  max-width: 600px;
  margin: 0 auto;
}

.hero .form-search .form-control {
  padding-top: 18px;
  padding-bottom: 18px;
  padding-left: 20px;
  padding-right: 20px;
  border: none;
  border-radius: 30px;
}

.hero .form-search .form-control:hover,
.hero .form-search .form-control:focus {
  outline: none;
  -webkit-box-shadow: none;
  box-shadow: none;
}

.hero .form-search .form-control {
  margin-right: 10px;
}

.hero .form-search .btn {
  background-color: black;

  padding-left: 30px;
  padding-right: 30px;
  color: #fff;
}

.hero .form-search .btn:hover,
.hero .form-search .btn:focus {
  outline: none;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.section {
  padding-top: 4rem;
  padding-bottom: 4rem; }
  .section .heading {
    font-weight: 500; }
    @media (max-width: 767.98px) {
      .section .heading {
        font-size: 36px; } }

</style>