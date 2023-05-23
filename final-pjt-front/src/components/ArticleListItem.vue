<template>
  <div>
    <div class="row">
    <p class="col-1 text-center" @click="goPage">{{ article.id }}</p>
    <p class="col-8" @click="goPage">{{ article.title }}</p>
    <p class="col-1 text-center" @click="goUser">{{ article.username }}</p>
    <p class="col-2 text-center">{{ createtime }}</p>
  </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  computed: {
    createtime() {
      return this.article.updated_at.slice(0, 10)
    }
  },  
  methods:{
    goUser() {
    this.$router.push(`/profile/detail/${this.article.username}`)
    },
    goPage() {
      this.$router.push({
      name: 'ArticleDetail',
      params: { id: this.article.id }
    })
    }
  }
}
</script>

<style scoped>
.text-center{
  margin-bottom: 0px;
}

.col-8 {
  margin-bottom: 0px;
}

.col-1:hover {
  text-decoration: underline;
  cursor: pointer;
}

.col-8:hover {
  text-decoration: underline;
  cursor: pointer;
}
</style>
