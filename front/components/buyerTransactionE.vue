<template>
  <v-card>
    <v-card-title>
      {{title}}
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        solo
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        rounded
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items=transactionemise
      :search="search"
      :items-per-page=5
      :options=
      "{sortBy: []}"
      :footer-props="{
        'items-per-page-text':'Transaction recu'
      }">
   
    </v-data-table>
  </v-card>
</template>
<script>
export default {
  props:{
    title:"",
    transactionemise:{
       type: []
     }
   },
  data() {
    return {
      search: '',
      headers: [
        { text: 'ref', value: 'ref' },
        { text: 'description', value: 'description' },
        { text: 'transaction_type', value: 'transaction_type' },
        { text: 'transaction_date', value: 'transaction_date' },
        { text: 'value', value: 'value' },
        { text: 'currency', value: 'currency' },
        { text: 'disbursement_channel', value: 'disbursement_channel' },
        { text: 'humanitarian', value: 'humanitarian' },

        
      ],
    }
  },
//   computed:{
//       ...mapState('project', {
//         amounts: state=> state.amounts,
//         errors: state=> state.errors
//       })
//     },
}
</script>