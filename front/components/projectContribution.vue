<template>
  <div>
    <Titre title="Bailleur et Contribution liées au projets" />
    <v-card class="container mx-auto px-3">
      <v-data-table
        :headers="headersContribution"
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
      
      headersContribution: [
        { text: 'Bailleur', value: 'name' },
        { text: 'Montant', value: 'value' },
        { text: 'Dévise', value: 'currency' },
        
      ],
    }
  },
}
</script>