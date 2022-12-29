import axios from 'axios'

export const state = () => ({
    particularName:'',

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
    organisationList : [],
    organisationDetails : [],
  })

export const mutations = {
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
    setOrganisationList(state, payload) {
        state.organisationList = payload
    },
    setOrganisationDetails(state, payload) {
        state.organisationDetails = payload
    },

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
}
export const getters = {}




// Colaboration : 
// etude : doc,url