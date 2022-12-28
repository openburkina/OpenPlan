<template>
  <div>
      <v-tabs
        v-model="tab"
        background-color="indigo lighten-5"
        centered
        icons-and-text
      >
        <v-tabs-slider></v-tabs-slider>

        <v-tab href="#tab-1">
          Infos Général
          <v-icon>mdi-axis-arrow-info</v-icon>
        </v-tab>
        <v-tab href="#tab-2">
          Secteur
          <v-icon>mdi-cash</v-icon>
        </v-tab>

        <v-tab href="#tab-3">
          Organismes
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>

        <v-tab href="#tab-4">
          Budget
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>

        <v-tab href="#tab-5">
          Condition
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>

        <v-tab href="#tab-6">
          Transactions
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>

        <v-tab href="#tab-7">
          Résultat
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>

        <v-tab href="#tab-8">
          Type Finance
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>

        <v-tab href="#tab-9">
          Type Aide
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" class="mb-9">
        <v-tab-item value="tab-1" class="mb-9">
          <ProjectInfo :info="info" />
        </v-tab-item>
        <v-tab-item value="tab-2">
          <ProjectSector  :search="search"  :items="items"/>
        </v-tab-item>
        <v-tab-item value="tab-3">
          <ProjectOrganisme  :search="search"  :items="organismes"/>
        </v-tab-item>
      </v-tabs-items>
  </div>
</template>
<script>
  import { mapState, mapActions } from 'vuex';

  export default {
    computed: {
      ...mapState({
        info: 'projectDetails',
        items: 'projectDetailsSector',
        organismes:'projectDetailsOrganisme',
      //  dates: 'projectStages',
      //  transactions: 'projectTransactions'
      })
    },

    mounted() {
      this.fetchProjectsDetails(this.id);
      this.fetchProjectsDetailsSector(this.id);
      this.fetchProjectsDetailsOrganisme(this.id);
    //  this.fetchProjectTransactions(this.id);
    },

    data() {
      return {
        search: '',
        id: this.$route.params.project,
        tab: null,
      }
    },

    methods: {
      ...mapActions([
        'fetchProjectsDetails',
        'fetchProjectsDetailsSector',
        'fetchProjectsDetailsOrganisme',
       // 'fetchProjectTransactions'
      ]),
      getTitle(message) {
        return `${message} sur le projet : ${this.id}`
      },
      getProjet() {
          console.log(this.id)
        return this.projets.find((p) => p.id == this.id)
      },
      getColor(statut) {
        if (statut < 1) return '#00E396'
        else return '#008FFB'
      },
      getValue(statut) {
        if (statut < 1) return 'mdi-close'
        else return 'mdi-check'
      },
    },
  }
</script>