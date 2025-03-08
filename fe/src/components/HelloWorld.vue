<template>
  <v-card height="100vh" class="d-flex flex-column justify-content-center align-center gap-4" color="transparent" flat>
    <div>
      <a href="https://vite.dev" target="_blank">
        <img src="/vite.svg" class="logo-custom" alt="Vite logo-custom" />
      </a>
      <a href="https://vuejs.org/" target="_blank">
        <img src="../assets/vue.svg" class="logo-custom vue" alt="Vue logo-custom" />
      </a>
      <a href="https://vuetifyjs.com" target="_blank">
        <img src="../assets/vuetify.svg" class="logo-custom vuetify" alt="Vue logo-custom" />
      </a>
    </div>

    <h1>{{ localdataStore.titulo }}</h1>
    <div class="d-flex justify-content-center align-center flex-column gap-3">
      <v-btn @click="">Vuetify button</v-btn>
    </div>
  </v-card>
</template>


<script>

import { useLocaldataStore } from '../stores/localdata';

export default {
  data() {
    return {
      titulo: false,
    };
  },
  setup() {
    const localdataStore = useLocaldataStore()
    return { localdataStore }
  },
  components: {
  },
  methods: {
  },
  mounted() {
  },
};
</script>
