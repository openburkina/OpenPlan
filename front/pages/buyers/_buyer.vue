<template>
  <Travaux 
  :done=done
  :transactemise=transactionemise
  :transactrecu=transactionrecu
  :pieStats=pieStats
  :barOneStats=barOneStats
  :barTwoStats=barTwoStats
  :lineStats=lineStats

  v-on:pie-year-change="fetchPieStats($event)"
  v-on:line-years-change="fetchLineStats($event)"
  v-on:barone-year-change="fetchBarOneStats($event)"
  v-on:bartwo-year-change="fetchBarTwoStats($event)"
  />
</template>
<script>
export default {
  data(){
    return {
        id: this.$route.params.buyer
    }
  },
  computed:{
    done(){
      return this.$store.state.organisationDetails
    },
    transactionrecu(){
      return this.$store.state.organisationTransactionR
    },
    transactionemise(){
      return this.$store.state.organisationTransactionE
    },
    pieStats() {
      return this.$store.state.organismePieStats
    },
    barOneStats() {
      return this.$store.state.organismeBarOneStats
    },
    barTwoStats() {
      return this.$store.state.organismeBarTwoStats
    },
    lineStats() {
      return this.$store.state.organismeLineStats
    }
  },
  mounted(){
    this.$store.dispatch('fetchOrganisationDetails',this.id)
    this.$store.dispatch('fetchOrganisationTransactionR',this.id)
    this.$store.dispatch('fetchOrganisationTransactionE',this.id)
    this.fetchPieStats(new Date().getFullYear())
    this.fetchBarOneStats(new Date().getFullYear())
    this.fetchBarTwoStats(new Date().getFullYear())
    this.fetchLineStats([new Date().getFullYear(), new Date().getFullYear()])
  },
  methods: {
    fetchPieStats(year) {
      this.$store.dispatch('fetchOrganismePieStats', { buyer_id: this.id, year })
    },
    fetchBarOneStats(year) {
      this.$store.dispatch('fetchOrganismeBarOneStats', { buyer_id: this.id, year })
    },
    fetchBarTwoStats(year) {
      this.$store.dispatch('fetchOrganismeBarTwoStats', { buyer_id: this.id, year })
    },
    fetchLineStats([startYear, endYear]) {
      this.$store.dispatch('fetchOrganismeLineStats', { buyer_id: this.id, start_year: startYear, end_year: endYear })
    },
  },
}
</script>
