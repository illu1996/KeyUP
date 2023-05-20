<template>
  <div>
    <h5>{{ article.id }}</h5>
    <P @click="goUser">작성자 : {{ article.username }}</P>
    <p>{{ article.title }}</p>
    <router-link :to="{
      name: 'ArticleDetail',
      params: { id : article.id }}">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  methods:{
    goUser() {
    this.$router.push(`/profile/detail/${this.article.username}`)
    },
  }
}
</script>

<style>

</style>
