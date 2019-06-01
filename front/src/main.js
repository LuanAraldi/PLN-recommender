import Vue from 'vue'
import VueSwal from 'vue-swal'
import App from './App.vue'

Vue.config.productionTip = false
Vue.use(VueSwal)

new Vue({
  render: h => h(App),
}).$mount('#app')
