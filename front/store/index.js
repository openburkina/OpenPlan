import axios from 'axios'

export const state = () => ({
    listProjets:[],
    tmpList:[], 
    detailsProjets: [],   

    projectList : [],
    projectDetails : [],
    projectDetailsSector : [],
    projectDetailsOrganisation : [],
    projectDetailsOrganisme : [],
    projectDetailsCondition : [],
    projectDetailsCollaboration : [],
    projectDetailsIndicateur : [],
    projectDetailsTransaction : []


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
/**
     * Liste des travaux
     */
     // setter de Liste de tous les travaux
     listOfProjects(state,paylaod){
        state.listProjets = paylaod
        state.listProjets.forEach((el) => {
            console.log(el)
            state.tmpList.push({
                id: e1.id,
                lang: e1.lang,
                default_currency: e1.default_currency,
                humanitarian: e1.humanitarian,
                iati_identifier:e1.iati_identifier,
                title: e1.title,
                description: e1.description,
                activity_status: e1.activity_status,
                activity_scope: e1.activity_scope     
            })
            
        })
        state.listProjets = state.tmpList
        state.tmpList = []
    },

    detailsOfProjects(state,paylaod){
        state.detailsProjets = paylaod
        state.detailsProjets.forEach((el) => {
            console.log(el)
            state.tmpList.push({
                id: e1.id,
                lang: e1.lang,
                default_currency: e1.default_currency,
                humanitarian: e1.humanitarian,
                iati_identifier:e1.iati_identifier,
                title: e1.title,
                description: e1.description,
                activity_status: e1.activity_status,
                activity_scope: e1.activity_scope,
                regionid3:e1.regionid3.continent,
                region_name:e1.regionid3.name,
                country:e1.countryid3.name
            })
            
        })
        state.detailsProjets = state.tmpList
        state.tmpList = []
    },

    /**
     * 
     * Travaux End
     * 
     */
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
}
export const getters = {}




// Colaboration : 
// etude : doc,url