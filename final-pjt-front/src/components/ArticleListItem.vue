<template>
  <div>
    <h5>{{ article.id }}</h5>
    <P>작성자 : {{ article.username }}</P>
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
  }
}
</script>

<style>

</style>
