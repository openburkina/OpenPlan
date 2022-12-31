<template>
  <div>
    <Titre title="Les Organismes liées au Projet" />
    <v-card class="container mx-auto px-3">
      <v-data-table
        :headers="headersOrgnanisme"
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
      
      headersOrgnanisme: [
        { text: 'id', value: 'organizationid.id' },
        { text: 'ref', value: 'organizationid.ref' },
        { text: 'type', value: 'organizationid.type' },
        { text: 'narrative', value: 'organizationid.narrative' },
        { text: 'discriminator', value: 'organizationid.discriminator' },
        { text: 'role', value: 'role' },
      ],
    }
  },
  methods: {
    createEditLink(buyer) {
      console.log(buyer)
      this.$store.state.particularName = `Projet de : ${buyer.organizationid.narrative }`
      return this.$router.push({ path: '/buyers/' + buyer.organizationid.id})
    },
  },
}
</script>