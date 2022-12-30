<template>
  <div>
    <Titre title="Les Activités liées au Projet" />
    <v-card class="container mx-auto px-3">
      <v-data-table
        :headers="headersChild"
        :items="items"
        :search="search"
        class="elevation-0"
        @click:row="createEditLink"
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
      
      headersChild: [
        { text: 'Region', value: 'regionid3.name' },
        { text: 'Pays', value: 'countryid3.name' },
        { text: 'Identifiant IATI', value: 'iati_identifier' },
        { text: 'Titre', value: 'title' },
        { text: 'Description', value: 'description' },
        { text: 'Status', value: 'activity_status' }
      ],
    }
  },
  methods: {
    createEditLink(project) {
      return this.$router.push({ path: '/projects/' + project.id})
    },
  },
}
</script>