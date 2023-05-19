<template>
  <div>
    <p>작성자 : {{ review.username }}</p>
    <p>{{ review.content }}</p>
  </div>
</template>

<script>
export default {
  name :'MovieDetailReviewItem',
  props : {
    review : Object,
  }
}
</script>

<style>

</style>