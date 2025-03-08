import { defineStore } from "pinia";

export const useLocaldataStore = defineStore("localdata", {
    state: () => {
        return {
            titulo: 'Vue + Flask + Vuetify'
        };
    },
    actions: {
        //funciones javascript
        limpiar() {
            this.$reset()
        }
    },
    getters: {
    },
    persist: {
        enabled: true,
        strategies: [{
            key: 'localdata_storaged',
            storage: sessionStorage,
        }]
    },
});