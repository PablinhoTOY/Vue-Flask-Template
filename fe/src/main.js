import { createApp } from 'vue';
import App from './App.vue';
import './style.css'
import 'vuetify/styles'
import { router } from './router'
import { createPinia } from "pinia";
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import { VNumberInput } from 'vuetify/labs/components'
import * as directives from 'vuetify/directives'
import { aliases, fa } from 'vuetify/iconsets/fa'
import { mdi } from 'vuetify/iconsets/mdi'
import '@mdi/font/css/materialdesignicons.css'
import '@fortawesome/fontawesome-free/css/all.css'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

// se puede utilizar MDI y font awesome
const vuetify = createVuetify({
    components: {
        ...components,
        VNumberInput,
    },
    icons: {
        defaultSet: 'fa',
        aliases,
        sets: {
            fa,
            mdi, //para mdi utilizar de esta manera "mdi:mdi-pencil"
        },
    },
    directives,
})

const app = createApp(App)
const pinias = createPinia()

// #################### COLORS #########################

app.config.globalProperties.backgroundColor = '#242424'

// #################### COLORS #########################

//app.config.globalProperties.manualBack = false

app.use(vuetify);
app.use(pinias);
app.use(router);

app.mount('#app');

