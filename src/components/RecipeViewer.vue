<template>
  <div id='recipe' style="height:100%;">
    <div class="top-spacer"></div>

    <div class="content">
        <div class="top-spacer"></div>
      <div class="description">

        <h2 class="recipe-header">{{ recipe.name }}</h2>
        <div class="bold" style="text-decoration:underline;text-decoration-style:dotted;margin-top:.5em;">
          <router-link class="author" :to="'/recipes/authors/' + recipe.author">{{ recipe.author }}</router-link>
        </div>
        <hr />

        <div>
          <div class="yieldbox">
          <p><span class="bold">Yield: </span>{{(recipe.recipeYield.length < 50)?recipe.recipeYield:recipe.recipeYield.slice(0,50) + "..."}}</p>
          <p><span class="bold">Time: </span>{{time}}</p>
        </div>
            <div class="starbox">
              <p><span class="bold">Rating: </span><span style="color:var(--bright);font-size:1.3em" v-for="i in recipe.rating">★</span><span style="color:var(--dark);font-size:1.3em" v-for="i in 5 - recipe.rating">☆</span> ({{formatRatingCount}})</p>
                </div>
        </div>
        <div id="imagebox">
          <img :src="recipe.image" class="on_mobile" alt="" />
          <p v-html="recipe.description"></p>
          <img :src="recipe.image" class='hide_on_mobile' alt="" />
        </div>
        <hr>
        <div id="keywords">

          <span v-for="keyword in keywords" :key="hash(keyword)"><router-link :to="'/recipes/categories/' + keyword">{{keyword}}</router-link>, </span>
        </div>
        <hr>
        <div id="recipebox">
          <div>
            <h3 style="width:335px;" class="inlineblock">Ingredients</h3>
            <h3 class="hide_on_mobile inlineblock">Preparations</h3>
          </div>

          <div id="ingredients">
            <li v-for="ingredient in ingredients" :key="hash(ingredient, seed=1)">
              <span class="quantity">{{ingredient[0]}} </span><span class="ingredient" v-html="ingredient[1]"></span>
          </li>
          </div>
          <div id="instructions">
            <h3 style="display:inline-block" class="on_mobile">Preparations</h3>
            <li v-for="(instruction, index) in instructions" :key="hash(instruction, seed=2)">
                <h4>Step {{index + 1}}</h4>
              <p v-html="instruction"></p>
          </li>
          </div>
        </div>
        <div class="top-spacer"></div>
        <div class="bottom-spacer"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DesignViewer",
  props: {},
  computed: {
    formatRatingCount() {
      let ratingCount = this.recipe.ratingCount
      ratingCount = ratingCount.toString().replaceAll(new RegExp(/(\d)(?=(\d{3})+$)/, 'g'), "$1,")
      return ratingCount
    },
    time() {
      let s = this.recipe.secondsToPrepare

      var date = new Date(null);
      date.setSeconds(s); // specify value for SECONDS here
      var results = date.toISOString().substr(11, 8).split(":");

      let tiers = ["hours","minutes","seconds"]
      let output = []

      for (let i in tiers) {
        let tier = tiers[i]
        let result = parseInt(results[i])
        if (result == 0) {
          continue
        }
        output.push(result.toString() + " " + tier)
      }

      return output.join(", ")
    },
    recipe_index() {
      let recipes = this.$root.$data.recipes;
      let name = this.$route.params.id;

      var i = recipes.findIndex(function(post, index) {
        if (post.name == name) return true;
      });
      return i;
    },
    recipe() {
      let recipes = this.$root.$data.recipes;
      return recipes[this.recipe_index];
    },
    keywords() {
      let recipe = this.$root.$data.recipes[this.recipe_index]
      return recipe.keywords.split(",").map(x => x.trim()).filter(x => x != " " & x != "")
    },
    instructions() {
      let recipe = this.$root.$data.recipes[this.recipe_index]
      if (recipe.instructions != null) {
        let instructions = recipe.instructions.replaceAll("\', \'", "\",\"").replaceAll("[\'","[\"").replaceAll("\']", "\"]").replaceAll("1/2", "½").replaceAll("1/4", "¼").replaceAll("\', \"", "\",\"").replaceAll("\", \'", "\",\"")
        instructions = JSON.parse(instructions)
        return instructions
      } else {
       return []
      }
    },
    ingredients() {
      let recipe = this.$root.$data.recipes[this.recipe_index]
      let ingredients = recipe.recipeIngredient.replaceAll(new RegExp(/<.*?>/, 'g'), "")
      ingredients = ingredients.replaceAll(new RegExp(/(["'],\s*['"])/, 'g'), "\", \"").replaceAll("[\'","[\"").replaceAll("\']", "\"]").replaceAll("1/2", "½").replaceAll("1/4", "¼").replaceAll(" ¼","¼").replaceAll(" ½", "½")
      console.log(ingredients)
      let ingredientArray = JSON.parse(ingredients)
      let newArray = []
      let quantityIngredient = []
      for (let i in ingredientArray) {
        quantityIngredient = ingredientArray[i].split(/^(.*?)(((\d-)|[a-zA-Z(]).*)$/)
        newArray.push(quantityIngredient.slice(1,3))
      }
      return newArray
    }
  },
  data() {
    return {};
  },
  methods: {
    hash(word, seed=0) {
      word = word.toString()
      let h1 = 0xdeadbeef ^ seed, h2 = 0x41c6ce57 ^ seed;
      for (let i = 0, ch; i < word.length; i++) {
          ch = word.charCodeAt(i);
          h1 = Math.imul(h1 ^ ch, 2654435761);
          h2 = Math.imul(h2 ^ ch, 1597334677);
      }
      h1 = Math.imul(h1 ^ (h1>>>16), 2246822507) ^ Math.imul(h2 ^ (h2>>>13), 3266489909);
      h2 = Math.imul(h2 ^ (h2>>>16), 2246822507) ^ Math.imul(h1 ^ (h1>>>13), 3266489909);
      return 4294967296 * (2097151 & h2) + (h1>>>0);
    }
  }
};
</script>

<style lang="css" scoped>
#recipe h1,h2,h3,h4,h5,h6 {
  font-family:ibm-plex-serif,serif;
}

hr {
margin:2em 0;
}

.yieldbox {
  display:inline-block;
  margin:0 0 1em 0;
}

.yieldbox p{
 margin:0;
}

.bold {
 font-weight:bolder;
 font-family: "ibm-plex-mono", mono;
}

.recipe-header {
  display: inline-block;
  margin-bottom: 0;
  padding-right: 0.3em;
}

#left-box {
  height: 100%;
}

img {
  padding: 0 0 1em 0;
  max-height: var(--site-width);
}

.date {
  display: inline;
  padding: 0 0.3em;
  color: var(--dark);
  font-size: 0.7em;
  font-weight: bolder;
  font-family: "ibm-plex-mono", mono;
}

.content {
  width: var(--site-width);
  position: absolute;
  margin: 0 calc((100vw - var(--site-width)) / 2);
  left: 0;
}

.flex-content {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  height: 100%;
  width: 100%;
}

.image_wrap {
  max-height: 100%;
}

.description {
  flex: 1;
  width: 100%;
  margin: 0 auto;
}

#imagebox {
margin-top:2em;
display:flex;
  align-items: flex-start;
}

#imagebox p{
 margin:0;
 width: 100%;
}

#imagebox img{
  margin-left:3em;
  width: calc(var(--site-width) - 355px);
}

.ingredient {
  vertical-align:top;
  display:inline;
  display:inline-block;
  width: calc(100% - 70px)
}

.quantity {
  font-family: "ibm-plex-mono", mono;
  padding-right: .6em;
  vertical-align:top;
  min-width: 70px;
  text-align:right;
  display:inline-block;
  height:100%;
  font-weight:bolder;
}

li {
  line-height: unset;
  margin: .5em 0;
}

#ingredients {
  font-size: .9em;
  list-style-type: none;
  vertical-align:top;
  width:300px;
  display:inline-block;
}

#instructions h4 {
  padding:0 0 .5em 0;
  margin:0;
}

#instructions li {
  margin:0 0 2em 0;
}

#instructions {
  display:inline-block;
  width: calc(100% - 300px);
  font-size: 1em;
  list-style-type: none;
  vertical-align:top;
  padding-left:35px;

}

.starbox p {
 margin:0;
}

.starbox {
 text-align:right;
 display:inline-block;
 float:right;
}

.on_mobile {
  display:none !important;
}

.inlineblock {
  display:inline-block;
}

.author {
 color: black;
 text-decoration-style: dotted;
}

.author:hover {
 color: var(--bright);
}


@media screen and (max-width: 1000px) {
  .inlineblock {
    display:unset;
  }

  .right {
    height: unset;
  }

  #left-box {
    height: unset;
    padding-bottom: 20vw;
  }

  .date::before {
    content: unset;
    color: black;
    font-size: 1em;
  }
  .content,
  .description,
  img {
    width: 100%;
    margin: 0 auto;
    position: unset;
    max-width: 100%;
    max-height: 80vh;
  }

  .yieldbox {
    margin:0;
    padding:0;
  }
  .starbox {
   text-align:unset;
   display:unset;
   float:unset;
  }

  #imagebox img{
    margin:1em 0 0 0;
    width:100%;
  }

  #imagebox {
    margin-top:0;
    display:flex;
    align-items: flex-start;
    flex-wrap:wrap;
  }

  #imagebox p{
   margin:0;
   width: 100%;
  }

  .on_mobile {
    width:100%;
    display:block;
  }

  .hide_on_mobile {
    display:none;
  }
  #instructions {
    width: 100%;
    padding:0;
  }

  #instructions p {
    margin:0 0 1em 0;
  }

  .ingredient {
   width: calc(100% - 30px - .6em);
  }
  .quantity {
    min-width:30px;
  }

}
</style>
