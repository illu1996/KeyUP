<template>
  <div>
    MovieView
    <router-link to="/movies/all">전체 영화</router-link> |
    <router-link to="/movies/genre">장르별</router-link> |
    <router-link to="/movies/latest">신작</router-link> |
    <router-link to="/movies/popular">인기</router-link> |


    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'MovieView',

}
</script>

<style>

</style>