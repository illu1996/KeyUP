<template>
  <div>
    인기 박스오피스 <button>더보기</button>
    <MainPopularListItem />
  </div>
</template>

<script>
import MainPopularListItem from './MainPopularListItem.vue'
export default {
  name:'MainPopularList',
  components : {
    MainPopularListItem,
  }
}
</script>

<style>

</style>