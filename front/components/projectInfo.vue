<template>
<div>
    <Titre title="A propos du projets" />
  <v-card class="mx-auto" max-width="900">
    <v-list-item>
      <v-list-item-title>ID</v-list-item-title>
      <v-list-item-subtitle>{{ info.id }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Identifiant IATI</v-list-item-title>
      <v-list-item-subtitle>{{ info.iati_identifier }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Intitulé</v-list-item-title>
      <v-list-item-subtitle>{{ info.title }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Description</v-list-item-title>
      <v-list-item-subtitle>{{ info.description }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Budget</v-list-item-title>
      <v-list-item-subtitle>{{ info.budget_not_provided }} {{ info.default_currency }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Statut</v-list-item-title>
      <v-list-item-subtitle>{{ info.activity_status }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Localisation</v-list-item-title>
      <v-list-item-subtitle>{{ info.regionid3.name }} // {{ info.countryid3.name }} </v-list-item-subtitle>
    </v-list-item>
  </v-card>
</div>

</template>
<script>
export default {
  props: ['info'],
  methods: {
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