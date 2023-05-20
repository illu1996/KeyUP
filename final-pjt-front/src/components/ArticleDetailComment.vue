<template>
  <div>
    <p>작성자 : {{ comment.username }}</p>
    <p>대충 내용 : {{ comment.content }}</p>
    <br>
  </div>
</template>

<script>
export default {
  name : 'ArticleDetailComment',
  props: {
    comment : Object,
  },
  data() {
    return {
      content : null,
    }
  },
  methods : {

  }
}
</script>

<style>

</style>