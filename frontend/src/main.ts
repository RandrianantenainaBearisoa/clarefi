import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import setupPrimevue from './plugins'

// Supports weights 100-900
import '@fontsource-variable/saira-stencil/wdth-italic.css';
// Primevue icons
import 'primeicons/primeicons.css'

const app = createApp(App)

app.use(router)
setupPrimevue(app)

app.mount('#app')
