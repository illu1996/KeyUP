<template>
  <div>
    <p>인기 박스오피스</p>
  <div id="carouselExample" class="carousel slide">
    <div class="carousel-inner">
      <div class="carousel-item " v-for="(chunk, index) in chunkedMovieList" :key="index" :class="{ active: index === currentIndex }">
        <div class="row d-flex justify-content-center">
          <div class="col-2" v-for="movie in chunk" :key="movie.id">
            <MainPopularListItem :movie="movie" />
          </div>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev" @click="previousSlide">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next" @click="nextSlide">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  </div>
</template>

<script>
import MainPopularListItem from '@/components/MainPopularListItem.vue'
import axios from 'axios';

export default {
  name: 'MainPopularList',
  data() {
    return {
      movieList: [],
      currentIndex: 0,
      itemsPerPage: 5,
    };
  },
  components: {
    MainPopularListItem,
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
    getPopularMovie() {
      axios({
        method:'get',
        url : 'https://api.themoviedb.org/3/movie/popular?language=ko-kr&page=1', 
        headers: {
          accept: 'application/json',
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
          },
        })
        .then((res) => {
          console.log(res.data);
          this.movieList = res.data.results;
        });
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
  },
  created() {
    this.getPopularMovie();
  },
};
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
</style>


