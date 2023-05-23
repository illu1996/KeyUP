<template>
  <div class="movie">

    <MovieListItem :class="`lst${index}`" v-for="(movie,index) in randomMovieList" :key="index" :movie="movie" />
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'
import axios from 'axios'
import _ from 'lodash'
const MY_URL = 'http://127.0.0.1:8000'
// const MY_KEY =''


export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data() {
    return {
      movieList: [],
      randomMovieList: []
    }
  },
  methods: {
    randomList() {
      this.randomMovieList = _.sampleSize(this.movieList, 11)
    },
    getMovieList() {
      axios({
        method: "GET",
        url: `${MY_URL}/movies/`
      })
        .then((res) => {
          this.movieList = res.data
          this.randomList()
          console.log(this.randomMovieList)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getMovieList()

  }
}
</script>

<style scoped>
.movie {
  box-sizing: border-box;

  padding :0px;

}
.lst0{
  margin :10px 10px 0px 20px;
  padding :0px;
  width: 460px;
  position: absolute;
  top : 130px;
  left: 780px;

}
.lst1{
  margin :10px 10px 0px 20px;
  padding :0px;
  width: 750px;
  top : 130px;
  left : 0px;
  position: absolute;
}
.lst2{
  margin :10px 10px 0px 20px;
  position: absolute;
  width: 460px;
  top : 130px;
  left : 1310px;
}
.lst3{
  margin :10px 10px 0px 20px;

  position: absolute;
  width: 460px;
  top : 130px;
  left : 1810px;
}
.lst4{
  margin :10px 10px 0px 20px;

  position: absolute;
  width: 960px;
  top :850px;
  left : 1310px;
}
.lst5{
  margin :10px 10px 0px 20px;
  position: absolute;
  width: 460px;
  top :900px;
  left : 780px;
}
.lst6{
  margin :10px 10px 0px 20px;
  position: absolute;
  width: 355px;
  top : 1300px;
  left : 390px;

}
.lst7{
  margin :10px 10px 0px 20px;
  position: absolute;
  width: 355px;
  top : 1300px;
  left : 0px;

}
.lst8{
  margin :10px 10px 0px 20px;
  position: absolute;
  width: 355px;
  top : 1850px;
  left : 390px;
}
.lst9{
  margin :10px 10px 0px 20px;
  position: absolute;
  width: 355px;
  top : 1850px;
  left : 0px;

}
.lst10{
  margin :10px 10px 0px 20px;
  position: absolute;
  width: 460px;
  top : 1680px;
  left : 780px;
}

</style>
