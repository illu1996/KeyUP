<template>
  <div >
    MainView
    <div>
      Box 메인 배네
    </div>
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