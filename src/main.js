import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import dataset from "./dataset.json";
import about from "./about.json";
import items from "./items.json";
//import recipes from "./recipes.json";
import VueMarkdown from "vue-markdown";
import recipe_txt from 'raw-loader!./recipes.txt';

function ceasar(string, shift) {
  let resultArray = []
  for (let i = 0; i < string.length; i++) {
    let code = string.charCodeAt(i) + shift
    resultArray.push(String.fromCharCode(code))
  }
  return resultArray.join("")
}

let shifted = ceasar(recipe_txt, -1)
var recipes = JSON.parse(shifted)

Vue.config.productionTip = false;
let data = {
  projects: dataset.sort(function(a, b) {
    return new Date(b.date) - new Date(a.date);
  }),
  about: about,
  show_art: false,
  show_photos: false,
  show_design: false,
  items: items,
  recipes: recipes,

  // spotify_streamgraph data objects
  importedJSON: [],
  artist_list: [],
  csv: "",
  top_artists: [],
  top_artists_keys: {},
  week_max: 0,
  new_width: 0,
  files_imported: []
};

// Globally register your component
Vue.component("vue-markdown", VueMarkdown);

new Vue({
  router,
  data,
  components: {
    VueMarkdown
  },
  render: h => h(App)
}).$mount("#app");
