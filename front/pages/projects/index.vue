<template>
  <div>
   <Titre title="Projets" />
    <v-card color="indigo lighten-5 elevation-0 mx-4 mt-4 mb-16">
      <v-card-title>
        Liste des Projets
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
        :items="projects"
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
import { mapActions } from 'vuex'

export default {
  data(){
    return {
      search:'',
      headers: [
        {
            align: 'start',
            sortable: false,
         
          },
        { text: 'Identifiant', value: 'id' },
        { text: 'Identifiant IATI', value: 'iati_identifier' },
        { text: 'Intitulé', value: 'title' },
        { text: 'Description', value: 'description' },
        { text: 'Status', value: 'activity_status' },
        { text: 'Portée Activitée', value: 'activity_scope' },
        { text: 'Humanitaire', value: 'humanitarian' },
        { text: 'Dévise', value: 'default_currency' },
        { text: 'Language', value: 'lang' },
      ],
    }
  },
  mounted(){
    this.fetchProjects();
  },
 
  computed:{
    projects(){
      return this.$store.state.projectList
    },
  },

  methods: {
    ...mapActions({
      fetchProjects: "fetchProjects"
    }),
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
    createEditLink(project) {
      return this.$router.push({ path: '/projects/' + project.id})
    }
  },
}
</script>
