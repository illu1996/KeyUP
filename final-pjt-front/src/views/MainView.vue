<template>
  <div>
    MainView
    <LatestList />
    <PopularList />

  </div>
</template>

<script>
import LatestList from '@/components/LatestList.vue'
import PopularList from '@/components/PopularList.vue'
export default {
  name: 'MainView',
  components : {
    LatestList,
    PopularList,
  }
}
</script>

<style>

</style>