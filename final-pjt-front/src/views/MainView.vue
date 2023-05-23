<template>
  <div id="all">
    <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="3000">
          <img src="@/assets/메인1.png" class="d-block w-100" alt="..." @click="golatest">
        </div>
        <div class="carousel-item" data-bs-interval="3000">
          <img src="@/assets/메인2.png" class="d-block w-100" alt="..." @click="goRecommend">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
        <span aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
    </div>
    <div class=" mt-3 mainlatest">
      <MainLatestList />
    </div>
    <div class="mainpopular">
      <MainPopularList />
    </div>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
      <span aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>

  </div>
</template>

<script>
import MainLatestList from '@/components/MainLatestList.vue'
import MainPopularList from '@/components/MainPopularList.vue'
export default {
  name: 'MainView',
  components: {
    MainLatestList,
    MainPopularList,
  },
  methods: {
    golatest() {
      this.$router.push('/movies/latest')
    },
    goRecommend() {
      this.$router.push('/recommend')
    }
  },
}
</script>

<style scoped>
.carousel {
  margin-bottom: 80px;
}

.mainlatest {
  margin-bottom: 100px;
}

.carousel-control-prev {
  width: 80px;
}

.carousel-control-next {
  width: 80px;
}
</style>