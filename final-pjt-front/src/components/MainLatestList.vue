<template>
  <div>
    <div>
      <div class="title-container d-flex justify-content-start align-items-end">
  <div class="title-line"></div>
  <span class="title-text ml-3">이달의 신작</span>
  <span class="more-link" @click="goLatest">더보기</span>
</div>
    </div>
    <div id="carouselExample" class="carousel slide">
      <div class="carousel-inner">
        <div class="carousel-item " v-for="(chunk, index) in chunkedMovieList" :key="index"
          :class="{ active: index === currentIndex }">
          <div class="row d-flex justify-content-center">
            <div class="col-2" v-for="movie in chunk" :key="movie.id">
              <MainLatestListItem :movie="movie" />
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev"
        @click="previousSlide">
        <span aria-hidden="true"><i class="bi bi-chevron-double-left"></i></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next"
        @click="nextSlide">
        <span aria-hidden="true"><i class="bi bi-chevron-double-right"></i></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>




<script>
import axios from 'axios';
import MainLatestListItem from './MainLatestListItem.vue'


export default {
  name: 'MainLatestList',
  components: {
    MainLatestListItem,
  },
  data() {
    return {
      movieList: [],
      currentIndex: 0,
      itemsPerPage: 5,
    }
  },
  computed: {
    chunkedMovieList() {
      const chunks = [];
      for (let i = 0; i < this.movieList.length; i += this.itemsPerPage) {
        const chunk = this.movieList.slice(i, i + this.itemsPerPage);
        chunks.push(chunk);
      }
      return chunks;
    },
  },
  methods: {
    getLatestMovie() {
      axios({
        method: 'get',
        url: "https://api.themoviedb.org/3/movie/now_playing?language=ko-kr&page=1",
        headers: {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        }
      })
        .then((res) => {
          console.log(res.data)
          this.movieList = res.data.results
        })
    },
    previousSlide() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
      }
    },
    nextSlide() {
      if (this.currentIndex < this.chunkedMovieList.length - 1) {
        this.currentIndex++;
      }
    },
    goLatest() {
      this.$router.push(`/movies/latest`)
    }
  },
  created() {
    this.getLatestMovie()
  },
}
</script>

<style scoped>
.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-color: black;
  width: 20px;
  height: 20px;
}

.carousel-control-prev-icon:before,
.carousel-control-next-icon:before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: inline-block;
  width: 10px;
  height: 10px;
  background-color: white;
  border-radius: 50%;
}

.carousel-control-prev-icon {
  margin-right: 5px;
}

.carousel-control-next-icon {
  margin-left: 5px;
}

.carousel-control-next,
.carousel-control-prev {
  color: black;
}

.title-container {
  margin-bottom: 10px;
  margin-left: 50px;
}

@media screen and (min-width: 768px) {
  .title-container {
    margin-left: 100px;
  }
}

@media screen and (min-width: 1200px) {
  .title-container {
    margin-left: 160px;
  }
}


.title-line {
  width: 3px;
  height: 28px;
  background-color: black;
  margin-right: 8px;
  margin-bottom: 7px;
  display: inline-block;
}

.title-text {
  font-weight: bold;
  font-size: 30px;
  margin-right: 10px;
  margin-bottom: 10px;
  padding: 0px;
  margin: 0px;
  margin-right: 10px;
}

.more-link {
  font-size: 18px;
  color: rgb(75, 75, 75);
}
</style>
