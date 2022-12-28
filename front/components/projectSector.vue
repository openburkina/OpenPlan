<template>
  <div>
    <Titre title="Secteur liées au travail" />
    <v-card class="container mx-auto px-3">
      <v-data-table
        :headers="headersSectors"
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
      
      headersSectors: [
        { text: 'code', value: 'sectorid.code' },
        { text: 'percentage', value: 'sectorid.percentage' },
        { text: 'narrative', value: 'sectorid.narrative' },
      ],
    }
  },
}
</script>