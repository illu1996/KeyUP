<template>
  <div>
    <div id="banner">
      <img src="@/assets/banner.png" alt="">
    </div>
    <div>
      <p>자유롭게 의견을 나누어 보세요</p>
    </div>
    <div>
      <router-link to="/community/list">전체글 보기</router-link>
      <br>
      <router-link to="/community/create">작성하기</router-link>
      <hr>
      <router-view></router-view>
    </div>

  </div>
</template>

<script>

export default {
  name: 'CommunityView',

  computed: {
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (!this.isLogin) {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'Login' })
      }
      // 로그인이 되어 있으면 getArticles action 실행
      // 로그인 X라면 login 페이지로 이동
    }
  }
}
</script>

<style scoped>
#banner {
  width: 100%;
}

#banner img {
  width: 100%;
  height: auto;
}
</style>