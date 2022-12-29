<template>
  <v-card>
    <v-card-title>
      {{title}}
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        solo
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        rounded
        
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items=done
      :search="search"
      :items-per-page=5
      :options=
      "{sortBy: []}"
      :footer-props="{
        'items-per-page-text':'Liste de projet'
      }">
   
    </v-data-table>
  </v-card>
</template>

<script>
export default {
   props:{
     title: "",
      
     done:{
       type: []
     }
   },
  data(){
    return {
      search: '',
      select:null,
      annee: 2018,
      items: [],
        headers: [
          {
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Codage IATI', value: 'activityid.iati_identifier' },
          { text: 'Pays', value: 'activityid.countryid3.name' },
          { text: 'Region', value: 'activityid.regionid3.name' },
          { text: 'Titre', value: 'activityid.title' },
          { text: 'Dévise', value: 'activityid.default_currency' },
          { text: 'Etape', value: 'activityid.activity_status' },
          { text: 'Dernière mise à jour', value: 'activityid.last_updated_datetime' },
        ],
    }
  },
  mounted(){
    for(this.annee;this.annee<2032;this.annee++){
      this.items.push(this.annee)
    }
  },
  computed:{},
  methods:{
    onChange(value){
     if(value.length!=0){
       console.log(this.$store.state.idRegion)
      //  this.$store.dispatch('',this.$store.state.idRegion)
     }
    }
  }
}
</script>

