<template>
  <div>
    <Titre title="Les Organismes liées au Projet" />
    <v-card class="container mx-auto px-3">
      <v-data-table
        :headers="headersOrgnanisme"
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
      
      headersOrgnanisme: [
        { text: 'ref', value: 'organizationid.ref' },
        { text: 'type', value: 'organizationid.type' },
        { text: 'narrative', value: 'organizationid.narrative' },
        { text: 'discriminator', value: 'organizationid.discriminator' },
        { text: 'role', value: 'role' },
      ],
    }
  },
}
</script>