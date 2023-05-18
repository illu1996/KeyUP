<template>
  <div>
    MainView
    <MainLatestList />
    <MainPopularList />

  </div>
</template>

<script>
import MainLatestList from '@/components/MainLatestList.vue'
import MainPopularList from '@/components/MainPopularList.vue'
export default {
  name: 'MainView',
  components : {
    MainLatestList,
    MainPopularList,
  }
}
</script>

<style>

</style>