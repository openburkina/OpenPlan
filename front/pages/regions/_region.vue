<template>
  <RegionHelper 
  :done=done 
  :decaissement=decaissement
  :transaction=transaction
  :pieStats= pieStats
  :barOneStats= barOneStats
  :barTwoStats= barTwoStats
  :lineStats= lineStats

  v-on:pie-year-change="fetchPieStats($event)"
  v-on:line-years-change="fetchLineStats($event)"
  v-on:barone-year-change="fetchBarOneStats($event)"
  v-on:bartwo-year-change="fetchBarTwoStats($event)"
  />
</template>

<script>
export default {
   validate({ params }){
       //return /^\d+$/.test(params.regions)
       return params
    },
  data(){
    return {
        id: this.$route.params.region
    }
  },
  computed:{
    done(){
      return this.$store.state.regionProject
    },
    decaissement(){
      return this.$store.state.regionDecaissement
    },
    transaction(){
      return this.$store.state.regionTransaction
    },
    pieStats() {
      return this.$store.state.regionPieStats
    },
    barOneStats() {
      return this.$store.state.regionBarOneStats
    },
    barTwoStats() {
      return this.$store.state.regionBarTwoStats
    },
    lineStats() {
      return this.$store.state.regionLineStats
    }
  },
  mounted(){
    this.fetchPieStats(new Date().getFullYear())
    this.fetchBarOneStats(new Date().getFullYear())
    this.fetchBarTwoStats(new Date().getFullYear())
    this.fetchLineStats([new Date().getFullYear(), new Date().getFullYear()])
    this.$store.dispatch('fetchRegionProject',this.id)
    this.$store.dispatch('fetchRegionTransaction',this.id)
    this.$store.dispatch('fetchRegionDecaissement', this.id)
  },
  methods: {
    fetchPieStats(year) {
      this.$store.dispatch('fetchRegionPieStats', { region_id: this.id, year })
    },
    fetchBarOneStats(year) {
      this.$store.dispatch('fetchRegionBarOneStats', { region_id: this.id, year })
    },
    fetchBarTwoStats(year) {
      this.$store.dispatch('fetchRegionBarTwoStats', { region_id: this.id, year })
    },
    fetchLineStats([startYear, endYear]) {
      this.$store.dispatch('fetchRegionLineStats', { region_id: this.id, start_year: startYear, end_year: endYear })
    },
  },
}
</script>
