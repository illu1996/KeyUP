<template>
  <div>
    {{ peopleName }}
  </div>
</template>

<script>
import axios from 'axios';
const korean = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/

export default {
  name: 'MovieDetailCast',
  data() {
    return {
      peopleName : null,
    }
  },
  props: {
    cast : Number,
    original_language : String,
  },
  methods: {
    getPeopleInfo() {
      axios({
        method:'get',
        url: `https://api.themoviedb.org/3/person/${this.cast}?language=ko-kr`,
        headers : {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMDVjMWRmOTg2NTkyMzcwM2I3ZThmYzk5NmM4YjRhMiIsInN1YiI6IjYzZDMxN2IxNWEwN2Y1MDA5ZTk4MDA3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YcCaSDAbUQtDs3hXhi0xmf0sAnBzQklq7dEIq1oTlNs"
        }
      })
      .then((res)=>{
        if (this.original_language ==='ko') {
          this.people = res.data
          for (let peoplename of res.data.also_known_as) {
            if (korean.test(peoplename)) {
              this.peopleName = peoplename
              break
            }  
          }
        } else {
          this.peopleName = res.data.name
        }
      })
    }
  },
  created() {
    this.getPeopleInfo()
  }
}
</script>

<style>

</style>