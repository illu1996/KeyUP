<template>
  <div>
    <select v-model="genre_id" class="form-select" aria-label="Default select example" @change="getGenreMovie">
      <option selected> 카테고리 선택</option>
      <option v-for="genre in genreList" :key="genre.id" :value="genre.id" >{{ genre.name }}</option>
    </select>
    <GenreListItem v-for="genreMovie in this.genreMovieList" :key="genreMovie.id" :genreMovie="genreMovie" />
  </div>
</template>

<script>
import GenreListItem from './GenreListItem.vue'
import axios from 'axios'
// import _ from 'lodash'
const MY_URL = 'http://127.0.0.1:8000'

export default {
  name: 'GenreList',
  components: {
    GenreListItem,
  },
  data() {
    return {
      genreList: [],
      genre_id:null,
      genreMovieList:[]
    }
  },
  methods: {
    getGenreList() {
      axios({
        method: "GET",
        url: `${MY_URL}/movies/genres/`
      })
        .then((res) => {
          console.log(res.data)
          this.genreList = res.data

        })
        .catch((err) => {
          console.log(err)
        })
    },
    getGenreMovie() {
      if (Number.isInteger(this.genre_id)){
        axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-kr&page=1&sort_by=popularity.desc&with_genres=${this.genre_id}`,
        headers: {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        }
      })
        .then((res) => {
          console.log(res.data)
          this.genreMovieList = res.data.results
        })
        .catch((err)=>{
          console.log(err)
        })
      }
    }
  },
  created() {
    this.getGenreList()
  }
}
</script>

<style></style>