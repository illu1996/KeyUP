<template>
  <div class="text-center">
    <nav>
      <router-link to="/movies/all">전체 영화</router-link> <span>|</span> 
      <router-link to="/movies/genre">장르별</router-link> <span>|</span> 
      <router-link to="/movies/latest">신작</router-link> <span>|</span> 
      <router-link to="/movies/popular">인기</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'MovieView',

}
</script>

<style scoped>
  nav {
    margin-top: 20px;

    display: inline-block;
    margin-bottom: 10px;
    text-align: center;
  }

  a {
    text-decoration: none;
    color: black;
    font-weight: bold;
    font-size: 1.25em;

    align-items: center;
  }
  a span {
    font-size: 1.5em;
  }
  
  a:hover{
    color: rgb(26, 124, 83);
  }
  a:focus{
    color: rgb(68, 92, 226);
  }
  a+span{
    margin-left: 10px;
    margin-right: 10px;
  }
</style>