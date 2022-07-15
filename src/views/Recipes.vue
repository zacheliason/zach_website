<template>
  <div>
    <div class="top-spacer"></div>

        <input @keyup.delete="deleteValue(`titlesInput`)" @keypress="suggestFilterTitles" @click="suggestFilterTitles" id="titlesInput" type="text" list="titlesList" value="" placeholder="enter a title...">
        <input style='font-size:1em;font-weight:bolder' @keyup.enter="onEnterKeyword" @click="suggestFilterKeywords" @keypress="suggestFilterKeywords" id="keywordsInput" type="text" list="keywordsList" value="" placeholder="enter a keyword...">
          <datalist id="titlesList"></datalist>
          <datalist id="keywordsList"></datalist>
        <div class="starbox">
        <p style="margin-bottom:0;display:inline-block">
            <span @click='clickstar(1)' id='1' class='fillstar'>★</span>
            <span @click='clickstar(2)' id='2' class='fillstar'>★</span>
            <span @click='clickstar(3)' id='3' class='fillstar'>★</span>
            <span @click='clickstar(4)' id='4' class='fillstar'>★</span>
            <span @click='clickstar(5)' id='5' class='fillstar'>★</span>
        </p>
        </div>
    <div class="toggle-container">
        <h2 style="height:auto"></h2><span id="random" @click="shuffleRecipes()">🎰</span><h2 v-for="filter in this.filters" class="toggle" @click="removeFilter(filter)">{{filter}}</h2>

    </div>
      <hr />
      <div id="middlebar">
          <div style="font-size:2em" @click="previouspage()" class='toggle'>⬅️</div>
          <div>{{formatRatingCount(num_recipes)}} recipes</div>
          <div style="font-size:2em;margin:0" @click="nextpage()" class='toggle'>➡️</div>
      </div>
    <hr />

    <div class="relative">
      <div v-if="show_items">
        <div class="items">
          <div v-for="recipe in recipes" :key="recipe.name" class="mobile-item-box">
            <div class='mobile-item-box'>
                <router-link :to="'/recipes/' + recipe.name" class="item" v-bind:style="'background: url(' + recipe.image +') no-repeat center top;'">
                <div class="recipe-card">
                    <h4>{{recipe.name}}</h4>
                    <h5>{{recipe.author}}</h5>
                    <br>
                    <h5><span style=";font-size:1.3em" v-for="i in recipe.rating">★</span><span style="font-size:1.3em" v-for="i in 5 - recipe.rating">☆</span><span class="light"> ({{formatRatingCount(recipe.ratingCount)}})</span> </h5>
                    <p class="invisible">:)</p>
                </div>
            </router-link></div>
          </div>
        </div>
        <hr>
        <div>{{num_pages}}</div>

      </div>
        <div v-else style="width:100%">
          <p class='mono'>no recipes fit the given filters.</p>
        </div>
      </div>

    <div class="bottom-spacer top-spacer"></div>
  </div>
</template>

<script>
export default {
  name: "Design",
  data: function() {
     return {
       perpage: 9,
       pageNumber: 0,
       filters: [],
       current_keywords: [],
       current_titles: [],
       titleFilter: "",
       applyShuffle: false,
       rating: 5,
       author: this.currentAuthor
     }
   },
   watch:{
    $route (to, from){
        this.author = this.currentAuthor
    }
   },

   created() {
      if (this.$route.params.id != "" & this.$route.params.id != null) {
        let path = this.$route.path
        if (path.indexOf("categories") != -1) {
          this.filters.push(this.$route.params.id)
        } else {
            this.author = this.$route.params.id
        }
      }
   },
  methods: {
    shuffleRecipes() {
        let value = document.getElementById("random").innerHTML
        document.getElementById("random").innerHTML = (value.includes("📁"))?"🎰":"📁"
        this.applyShuffle = !this.applyShuffle
    },
    shuffle(array) {
      for (let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array
    },
    clickstar(id) {
    this.rating = id
      id++
      let el = null
      for (let i = 1; i <= 5; i++) {
        if (i < id) {
            el = document.getElementById(i.toString())
            el.innerHTML = "★"
            el.classList.remove('outlinestar');
            el.classList.add('fillstar');
        } else {
            el = document.getElementById(i.toString())
            el.innerHTML = "☆"
            el.classList.remove('fillstar');
            el.classList.add('outlinestar');
        }
      }
    },
    removeFilter(filter) {
        if (filter == this.$route.params.id) {
            this.$route.params.id == ""
        }
        this.filters = this.filters.filter(x => x != filter)
    },
    onEnterKeyword() {
        let value = document.getElementById("keywordsInput").value
        if (!this.filters.includes(value)) {
            this.filters.push(value)
        }
        document.getElementById("keywordsInput").value = ""
        this.suggestFilterKeywords()
    },
    deleteValue(id) {
      this.titleFilter = document.getElementById(id).value
    },
    suggestFilterTitles() {
      this.pageNumber = 0
      let value = document.getElementById("titlesInput").value.toLowerCase()
      let filtered_titles = Array.from(this.titles).filter(x => x.includes(value))
      let fillValue = ""
      for (let title of filtered_titles) {
        fillValue += "<option value='" + title + "'>" + title + "</option>"
      }
      document.getElementById("titlesList").innerHTML = fillValue
      this.titleFilter = value
    },
    suggestFilterKeywords() {
      this.pageNumber = 0
      let value = document.getElementById("keywordsInput").value.toLowerCase()
      let filtered_keywords = this.keywords.filter(x => x.includes(value))

      filtered_keywords = filtered_keywords.filter(x => !this.filters.includes(x) & x != "")
      filtered_keywords = this.shuffle(filtered_keywords)

      let fillValue = ""
      for (let keyword of filtered_keywords) {
        keyword = keyword.trim()
        fillValue += "<option value='" + keyword + "'>" + keyword + "</option>"
      }
      document.getElementById("keywordsList").innerHTML = fillValue
    },
    previouspage() {
      if (this.pageNumber > 0) {
          this.pageNumber--
      }
    },
    nextpage() {
      let lengthItems = this.filtered_recipes.length
      if (Math.ceil(lengthItems / this.perpage) > this.pageNumber + 1) {
          this.pageNumber++
      }
    },
    toggle_art() {
      this.pageNumber = 0
      this.$root.$data.show_art = !this.$root.$data.show_art;
    },
    toggle_photos() {
      this.pageNumber = 0
      this.$root.$data.show_photos = !this.$root.$data.show_photos;
    },
    toggle_design() {
      this.pageNumber = 0
      this.$root.$data.show_design = !this.$root.$data.show_design;
    },
    formatRatingCount(ratingCount) {
      if (ratingCount == null) {
          return 0
      }
      ratingCount = ratingCount.toString().replaceAll(new RegExp(/(\d)(?=(\d{3})+$)/, 'g'), "$1,")
      return ratingCount
    },
  },
  computed: {
    currentAuthor() {
      if (this.$route.params.id != "" & this.$route.params.id != null) {
        let path = this.$route.path
        if (path.indexOf("categories") != -1) {
            return null
        } else {
            return this.$route.params.id
        }
      }
        return null
    },
    maxRange() {
      let recipes = this.filtered_recipes
      recipes = recipes.map(x => x.ratingCount)
      return Math.max(recipes)
    },
    num_recipes() {
      let numRecipes = this.filtered_recipes.length
      return numRecipes
    },
    num_pages() {
      let numRecipes = this.filtered_recipes.length
      let numPages = Math.floor(numRecipes / this.perpage) + 1
      return (this.pageNumber + 1).toString() + " of " + numPages.toString() + " pages"
    },
    titles() {
      let recipes = this.filtered_recipes
      let t = recipes.map(x => x.name)
      t = new Set(t.join(", ").toLowerCase().split(", "))
      this.current_titles = t
      return t
    },
    keywords() {
      let recipes = this.filtered_recipes
      let k = recipes.map(x => x.keywords)
      k = Array.from(new Set(k.join(", ").toLowerCase().split(", ")))
      this.current_keywords = k
      return k
    },
    show_items() {
      return this.recipes.length > 0;
    },

    filtered_recipes() {
      let recipes = this.$root.$data.recipes

      if (this.titleFilter != "") {
          recipes = recipes.filter(x => x.name.toLowerCase().includes(this.titleFilter))
      }

      if (this.author != null) {
          recipes = recipes.filter(x => x.author != null)
          recipes = recipes.filter(x => x.author.toLowerCase().includes(this.author.toLowerCase()))
      }

      recipes = recipes.filter(x => x.rating == this.rating)
      recipes = recipes.filter(x => x.keywords != null)
      recipes = recipes.filter(x =>
          this.filters.every(val => x.keywords.includes(val))
      )

      if (this.applyShuffle) {
        recipes = this.shuffle(recipes)
      }

      return recipes
    },
    recipes() {
      let recipes = this.filtered_recipes
      recipes = recipes.slice(this.pageNumber*this.perpage,this.pageNumber*this.perpage+this.perpage)
      /*recipes.sort(function(b, a){return b.name.length - a.name.length})*/
      return recipes
    },
    show_photos() {
      return this.$root.$data.show_photos;
    },
    show_art() {
      return this.$root.$data.show_art;
    },
    show_design() {
      return this.$root.$data.show_design;
    }
  }
};
</script>


<style lang="css" scoped>
.starbox {
 width:328px;
 display:flex;
 justify-content:space-between;
 align-items: end;
}

#random {
 font-size:2em;
 cursor:pointer;
 display:inline-block;
 float:right;
 margin:0 1em 0 0;
}

.toggle:hover {
  color: var(--bright);
}

.toggle-container {
  display:flex;
  flex-wrap:wrap;
  margin-bottom:1em;
}

.toggle {
  margin: .2em 2em 0 0;
  cursor: pointer;
  color: var(--dark);
}

.active {
  color: var(--bright);
}


.item h4 {
    font-size:.9em;
    margin:0;
    height:70px;
}

.item:hover .recipe-card {
    border-color:var(--bright);
}
.recipe-card {
    background-color:var(--grey);
    padding:.7em 1em;
    margin:0;
    border: 3px solid var(--dark);
    border-top:0;
}

.item {
    box-sizing:border-box;
  line-height:1em;
    border: inset 3px solid var(--dark);
    border-bottom:0;
  display: inline-block;
  margin-top: 0;
  background-color: var(--grey);
  width: calc((var(--site-width) - 2em) / 3);
  padding-top: 95%;
  height: 0;
  background-size: cover !important;
  cursor: pointer;
}

/*
.items:hover > *:not(:hover) {
  opacity: .9 !important;
}
*/

.square_overlay:hover {
  opacity: 1;
}

.relative {
  position: relative;
}

.outlinestar {
    color:var(--dark);
    font-size:2em;
    cursor:pointer;
}

#middlebar div{
 margin:0;
}
#middlebar {
 display:flex;
 justify-content:space-between;
 align-items:center;
}

.fillstar {
    color:var(--bright);
    font-size:2em;
    cursor:pointer;
}

.mobile-item-box {
   margin-top:.75em;
}

.items {
  display: flex;
  margin-top: 1em;
  justify-content: space-between;
  -moz-column-gap: .5em;
  -webkit-column-gap: .5em;
  column-gap: 1em;
  height: auto;
  flex-wrap: wrap;
  margin-bottom:2em;
}

h4 {
    font-weight:normal;
    margin-bottom:0;
    padding-bottom:0;
}

.light {
 font-weight: 200;
 font-family: "ibm-plex-mono", mono;
}


h5 {
display:inline-block;
    margin:0;
    padding:0;
}

.nowrap-flex {
    display:flex;
    wrap:nowrap;
}
.invisible {
  opacity:0;
  height:.4em;
  margin:0;
  padding:0;
}

input {
    color: var(--dark);
    font-size: 1.5em;
    border: 0;
    outline: none;
    padding: 10px 20px;
    background-color: var(--grey);
    margin:.5em 0em;
    font-family:ibm-plex-mono;
    display:block;
}
@media screen and (max-width: 1000px) {
  .h-flex {
    display: block;
  }

  .square_overlay {
    width: calc(85vw);
  }

  .item {
    width: 100%;
  }

  .content,
  .description {
    width: 90%;
    margin: 0 5%;
  }

  #titlesInput {
    width:100%;
  }

  .item h4 {
    font-size:1.2em;
    line-height: 1em;
    margin-bottom:.2em;
  }

  .item h5 {
    font-size: 1em;
    line-height: 1.5em;
  }
  .mobile-item-box {
       width:100%;
   }

}
</style>
