<template>
  <div>
    <Titre title="Transactions liées au projets" />
    <v-card class="container mx-auto px-3">
      <v-data-table
        :headers="headersDecaissements"
        :items="items"
        :search="search"
        class="elevation-0"
      >
      </v-data-table>
    </v-card>
  </div>
</template>
<script>
export default {
  props: ['search', 'items'],
  data() {
    return {
      
      headersDecaissements: [
        { text: 'ref', value: 'ref' },
        { text: 'description', value: 'description' },
        { text: 'transaction_type', value: 'transaction_type' },
        { text: 'transaction_date', value: 'transaction_date' },
        { text: 'value', value: 'value' },
        { text: 'currency', value: 'currency' },
        { text: 'Donneur', value: 'organizationid2.narrative' },
        { text: 'Receveur', value: 'organizationid.narrative' },
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