<template>
  <div>
    <Titre title="Conditions liées au projets" />
    <v-card class="container mx-auto px-3">
      <v-data-table
        :headers="headersConditons"
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
      
      headersConditons: [
        { text: 'type', value: 'conditionid.type' },
        { text: 'condition', value: 'conditionid.condition' },
        { text: 'attached', value: 'conditionid.attached' },

        
      ],
    }
  },
//   computed:{
//       ...mapState('project', {
//         amounts: state=> state.amounts,
//         errors: state=> state.errors
//       })
//     },
}
</script>