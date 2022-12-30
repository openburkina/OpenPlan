import axios from 'axios'
import { pieStatAdapter, lineStatAdapter, barStatAdapter } from '~/helpers/Adapters'
export const state = () => ({
    particularName:'',
//API BAILLEUR,REGION,PROJET
    projectList : [],
    projectDetails : [],
    projectDetailsSector : [],
    projectDetailsOrganisation : [],
    projectDetailsOrganisme : [],
    projectDetailsCondition : [],
    projectDetailsCollaboration : [],
    projectDetailsIndicateur : [],
    projectDetailsTransaction : [],
    projectDetailsContribution : [],
    projectDetailsChild : [],
    projectDetailsDecaissement : [],
    projectDetailsDecaissementEcart : [],
    organisationList : [],
    organisationDetails : [],
//END
//STATISTIQUE GRAPHIQUE
    organismePieStats: {'labels': [], 'data': []},
    organismeBarOneStats: {'labels': [], 'data': []},
    organismeBarTwoStats: {'labels': [], 'data': []},
    organismeLineStats: {'labels': [], 'data': []},
    homePieStats: {'labels': [], 'data': []},
    homeBarOneStats: {'labels': [], 'data': []},
    homeBarTwoStats: {'labels': [], 'data': []},
    homeLineStats: {'labels': [], 'data': []},
    
//END
  })

export const mutations = {
//Setter Stats Tableau
    setProjectList(state, payload) {
        state.projectList = payload
    },
    setProjectDetails(state, payload) {
        state.projectDetails = payload
    },
    setProjectDetails(state, payload) {
        state.projectDetails = payload
    },
    setProjectDetailsSector(state, payload) {
        state.projectDetailsSector = payload
    },
    setProjectDetailsOrganisation(state, payload) {
        state.projectDetailsOrganisation = payload
    },
    setProjectDetailsOrganisme(state, payload) {
        state.projectDetailsOrganisme = payload
    },
    setProjectDetailsTransaction(state, payload) {
        state.projectDetailsTransaction = payload
    },
    setProjectDetailsCondition(state, payload) {
        state.projectDetailsCondition = payload
    },
    setProjectDetailsCollaboration(state, payload) {
        state.projectDetailsCollaboration = payload
    },
    setProjectDetailsIndicateur(state, payload) {
        state.projectDetailsIndicateur = payload
    },
    setProjectDetailsContribution(state, payload) {
        state.projectDetailsContribution = payload
    },
    setProjectDetailsChild(state, payload) {
        state.projectDetailsChild = payload
    },
    setProjectDetailsDecaissement(state, payload) {
        state.projectDetailsDecaissement = payload
    },
    setProjectDetailsDecaissementEcart(state, payload) {
        state.projectDetailsDecaissementEcart = payload
    },
    setOrganisationList(state, payload) {
        state.organisationList = payload
    },
    setOrganisationDetails(state, payload) {
        state.organisationDetails = payload
    },
//End Stats Tableau

//Start Stat Graphique Setters
    setOrganismePieStats(state, payload) {
        state.organismePieStats = payload.data
    },
    setOrganismeBarOneStats(state, payload) {
        state.organismeBarOneStats = payload.data
    },
    setOrganismeBarTwoStats(state, payload) {
        state.organismeBarTwoStats = payload.data
    },
    setOrganismeLineStats(state, payload) {
        state.organismeLineStats = payload.data
    },

    setHomePieStats(state, payload) {
        state.homePieStats = payload.data
    },
    setHomeBarOneStats(state, payload) {
        state.homeBarOneStats = payload.data
    },
    setHomeBarTwoStats(state, payload) {
        state.homeBarTwoStats = payload.data
    },
    setHomeLineStats(state, payload) {
        state.homeLineStats = payload.data
    },
//End

}
export const actions = {
    async fetchProjects({ commit }) {
        await axios.get(
            `http://localhost:8000/api/projets`
        ).then(res => {
            commit("setProjectList", res.data)
        })
    },

    async fetchProjectsDetails({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}`
        ).then(res => {
            commit("setProjectDetails", res.data)
        })
    },

    async fetchProjectsDetailsSector({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/sector`
        ).then(res => {
            commit("setProjectDetailsSector", res.data)
        })
    },

    async fetchProjectsDetailsOrganisation({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/organisation`
        ).then(res => {
            commit("setProjectDetailsOrganisation", res.data)
        })
    },

    async fetchProjectsDetailsOrganisme({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/organisme`
        ).then(res => {
            commit("setProjectDetailsOrganisme", res.data)
        })
    },

    async fetchProjectsDetailsTransaction({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/transaction`
        ).then(res => {
            commit("setProjectDetailsTransaction", res.data)
        })
    },

    async fetchProjectsDetailsCondition({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/condition`
        ).then(res => {
            commit("setProjectDetailsCondition", res.data)
        })
    },

    async fetchProjectsDetailsCollaboration({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/collaboration`
        ).then(res => {
            commit("setProjectDetailsCollaboration", res.data)
        })
    },

    async fetchProjectsDetailsIndicateur({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/indicateur`
        ).then(res => {
            commit("setProjectDetailsIndicateur", res.data)
        })
    },

    async fetchProjectsDetailsContribution({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/contribution`
        ).then(res => {
            commit("setProjectDetailsContribution", res.data)
        })
    },

    async fetchProjectsDetailsChild({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/child`
        ).then(res => {
            commit("setProjectDetailsChild", res.data)
        })
    },


    async fetchProjectsDetailsDecaissement({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/decaissement`
        ).then(res => {
            commit("setProjectDetailsDecaissement", res.data)
        })
    },

    async fetchProjectsDetailsDecaissementEcart({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/decaissementecart`
        ).then(res => {
            commit("setProjectDetailsDecaissementEcart", res.data)
        })
    },

    async fetchOrganisation({ commit }) {
        await axios.get(
            `http://localhost:8000/api/projets/organisation`
        ).then(res => {
            commit("setOrganisationList", res.data)
        })
    },

    async fetchOrganisationDetails({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/activite`
        ).then(res => {
            commit("setOrganisationDetails", res.data)
        })
    },

        // Organisme Stats
    async fetchOrganismePieStats({ commit }, {buyer_id, year }) {
        await axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/activite/by_status?year=${year}`
        ).then(res => {
            commit("setOrganismePieStats", {name: "pie", data : pieStatAdapter(res.data)})
        })
    },
    async fetchOrganismeBarOneStats({ commit }, { buyer_id, year }) {
        axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/activite/by_regiontransact?year=${year}`
        ).then(res => {
            commit("setOrganismeBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
        })
    },
    async fetchOrganismeBarTwoStats({ commit }, {buyer_id, year }) {
        axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/activite/by_region?year=${year}`
        ).then(res => {
            commit("setOrganismeBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
        })
    },
    async fetchOrganismeLineStats({ commit }, {buyer_id, start_year, end_year }) {
        await axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/activite/by_sector?start_year=${start_year}&end_year=${end_year}`
        ).then(res => {
            commit("setOrganismeLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
        })
    },
        // End Organisme Stats
    
            // Organisme Stats
    async fetchOrganismePieStats({ commit }, {buyer_id, year }) {
        await axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/activite/by_status?year=${year}`
        ).then(res => {
            commit("setOrganismePieStats", {name: "pie", data : pieStatAdapter(res.data)})
        })
    },
    async fetchOrganismeBarOneStats({ commit }, { buyer_id, year }) {
        axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/activite/by_regiontransact?year=${year}`
        ).then(res => {
            commit("setOrganismeBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
        })
    },
    async fetchOrganismeBarTwoStats({ commit }, {buyer_id, year }) {
        axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/activite/by_region?year=${year}`
        ).then(res => {
            commit("setOrganismeBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
        })
    },
    async fetchOrganismeLineStats({ commit }, {buyer_id, start_year, end_year }) {
        await axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/activite/by_sector?start_year=${start_year}&end_year=${end_year}`
        ).then(res => {
            commit("setOrganismeLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
        })
    },
        // End Organisme Stats
        // Home Stats
        async fetchHomePieStats({ commit }, {year }) {
            await axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_status?year=${year}`
            ).then(res => {
                commit("setHomePieStats", {name: "pie", data : pieStatAdapter(res.data)})
            })
        },
        async fetchHomeBarOneStats({ commit }, {year }) {
            axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_regiontransact?year=${year}`
            ).then(res => {
                commit("setHomeBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
            })
        },
        async fetchHomeBarTwoStats({ commit }, {year }) {
            axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_sectortransact?year=${year}`
            ).then(res => {
                commit("setHomeBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
            })
        },
        async fetchHomeLineStats({ commit }, {start_year, end_year }) {
            await axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_sector?start_year=${start_year}&end_year=${end_year}`
            ).then(res => {
                commit("setHomeLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
            })
        },
        // End Home Stats
        
}
export const getters = {}




// Colaboration : 
// etude : doc,url