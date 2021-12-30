import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import dataset from './dataset.json'
import items from './items.json'
import VueMarkdown from 'vue-markdown'

Vue.config.productionTip = false;
let data = {
  projects: dataset.sort(function(a, b) {
    return new Date(b.date) - new Date(a.date);
  }),
  show_art: false,
  show_photos: false,
  show_design: false,
  items: items,
}

// Globally register your component
Vue.component('vue-markdown', VueMarkdown);

new Vue({
  router,
  data,
  components: {
    VueMarkdown,
  },
  render: h => h(App)
}).$mount("#app");
