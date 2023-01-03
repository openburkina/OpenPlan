<template>
  <div>
    <Titre title="Localités" />
    <v-card color="indigo lighten-5 elevation-4 mx-4 mt-4 mb-16">
      <v-card-title>
        Liste des localités
        
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Recherche"
          hide-details
          solo
          rounded
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="regions"
        :search="search"
        :items-per-page=5
        :options=
        "{sortBy: []}"
        class="elevation-1"
        @click:row="createEditLink"
      >
        <template v-slot:[`item.statut`]="{ item }">
          <v-chip :color="getColor(item.statut)" dark>
            <v-icon size="24px">
              {{ getValue(item.statut) }}
            </v-icon>
          </v-chip>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
export default {
  data(){
    return {
      search:'',
      headers: [
        {
            align: 'start',
            sortable: false,
         
          },
        { text: 'ID', value: 'id' },
        { text: 'Pays', value: 'countryid3.name' },
        { text: 'Localité Parente', value: 'locationid.name' },
        { text: 'Localité', value: 'name' },
        { text: 'Code Administratif', value: 'administrative_code' },
        
      ],
    }
  },

  mounted(){
     this.$store.dispatch('fetchRegion')
  },
 
  computed:{
    regions(){
      return this.$store.state.regionList
    },
   
  },
  methods: {
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
    createEditLink(region) {
      this.$store.state.regionName = `Localité de : ${region.name}`
      return this.$router.push({path: '/regions/' +region.id})

    }
  }
}

</script>