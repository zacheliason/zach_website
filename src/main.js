import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import dataset from "./dataset.json";
import about from "./about.json";
import items from "./items.json";
//import recipes from "./recipes.json";
import VueMarkdown from "vue-markdown";
import recipe_txt from 'raw-loader!./recipes.txt';

var CryptoJS = require("crypto-js")
const cjson = require('compressed-json')

let decompressed_recipes = cjson.decompress.fromString(recipe_txt)
var bytes  = CryptoJS.AES.decrypt(decompressed_recipes, 'zacheliason');
var recipes = JSON.parse(bytes.toString(CryptoJS.enc.Utf8));

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
