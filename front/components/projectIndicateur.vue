<template>
  <div>
    <Titre title="Indicateurs Resultats liées au projets" />
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
        { text: 'Type Resultat', value: 'resultsid.type' },
        { text: 'Resultat', value: 'resultsid.title' },
        { text: 'Indicateur', value: 'title' },
        { text: 'Description', value: 'description' },
        { text: 'Ascendant', value: 'ascending' },
        { text: 'Aggregation', value: 'aggregation_status' },
        { text: 'Code', value: 'code' },
        
      ],
    }
  },
}
</script>