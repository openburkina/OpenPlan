<template>
  <div>
    <Titre title="Type Collaboration liées au projets" />
    <v-card class="container mx-auto px-3">
      <v-data-table
        :headers="headersCollaboration"
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
      
      headersCollaboration: [
        { text: 'Libelle', value: 'collaboration_typeid.code' },
        
      ],
    }
  },
}
</script>