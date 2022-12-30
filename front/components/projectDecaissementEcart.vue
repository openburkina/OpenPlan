<template>
  <div>
    <Titre title="Décaissement liées au projets" />
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
        { text: 'Montant Prévu', value: 'valueprevue' },
        { text: 'Montant Décaissé', value: 'valuedisbursement' },
        { text: 'Difference', value: 'difference' },      
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