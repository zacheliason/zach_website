<template>
  <div>
    <div class="top-spacer"></div>

    <h2>design</h2>
    <hr>

    <div id="middlebar">
      <div style="font-size:2em" @click="previouspage()" class='toggle'>⬅️</div>
              <h2
        v-bind:class="{ active: show_photos }"
        class="toggle"
        @click="toggle_photos()"
      >
        🎞 photos
      </h2>
      <h2
        v-bind:class="{ active: show_design }"
        class="toggle"
        @click="toggle_design()"
      >
        💻 design
      </h2>
      <h2
        v-bind:class="{ active: show_art }"
        class="toggle"
        @click="toggle_art()"
      >
        🖼 art
      </h2>
      <div style="font-size:2em;margin:0" @click="nextpage()" class='toggle'>➡️</div>
    </div>
    <hr>

    <div class="relative">
      <div class="square_overlays">
        <div class="items">
          <div v-for="item in items" :key="item.id">
            <div class="square_overlay"></div>
          </div>
        </div>
      </div>

      <div class="items">
        <div v-if="show_items">
        <div class="items">
          <div v-for="item in items" :key="item.id">
            <router-link :to="'/design/' + item.name"
              ><div
                class="item"
                v-bind:style="
                  'background: url(/images/' +
                    item.image[0] +
                    ') no-repeat center top;'
                "
              ></div
            ></router-link>
          </div>
        </div>
        </div>
        <div v-else style="width:100%">
          <p class='mono'>toggle a category to view items.</p>
        </div>
      </div>
    </div>

    <br>
    <div>{{num_pages}}</div>

    <div class="bottom-spacer top-spacer"></div>
  </div>
</template>

<script>
export default {
  name: "Design",
  data: function() {
     return {
       perpage: 6,
       pageNumber: 0
     }
   },
  methods: {
    previouspage() {
      let lengthItems = this.filtered_items.length
      if (this.pageNumber > 0) {
          this.pageNumber--
      } else{
      console.log("NO")
      }
    },
    nextpage() {
      let lengthItems = this.filtered_items.length
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
    contains_object(obj, list) {
      var i;
      for (i = 0; i < list.length; i++) {
        if (list[i] === obj) {
          return true;
        }
      }
      return false;
    }
  },
  computed: {
    num_pages() {
      let numRecipes = this.filtered_items.length
      let numPages = Math.floor(numRecipes / this.perpage) + 1
      return (this.pageNumber + 1).toString() + " of " + numPages.toString() + " pages"
    },
    show_items() {
      return this.items.length > 0;
    },
    filtered_items() {
      let items = [];
      if (this.$root.$data.show_art) {
        items = items.concat(
          this.$root.$data.items.filter(item =>
            this.contains_object("art", item.category)
          )
        );
      }
      if (this.$root.$data.show_photos) {
        items = items.concat(
          this.$root.$data.items.filter(item =>
            this.contains_object("photo", item.category)
          )
        );
      }
      if (this.$root.$data.show_design) {
        items = items.concat(
          this.$root.$data.items.filter(item =>
            this.contains_object("design", item.category)
          )
        );
      }
      let items_set = new Set(items);
      items = Array.from(items_set).sort(function(a, b) {
        return new Date(b.date) - new Date(a.date);
      });
      return items;
    },
    items() {
      let items = this.filtered_items

      items = items.slice(this.pageNumber*this.perpage,this.pageNumber*this.perpage+this.perpage)
      return items;
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
.toggle {
  cursor: pointer;
  color: var(--dark);
}

.active {
  color: var(--bright);
}

.item {
  display: inline-block;
  margin-top: 1.5em;
  width: calc((var(--site-width) - 4em) / 3);
  padding-top: 95%;
  height: 0;
  background: url(/images/iceberg.jpg);
  background-size: cover !important;
  cursor: pointer;
  background: red;
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
}

.item:hover {
  mix-blend-mode: screen;
  filter: contrast(1.5) grayscale(100%);
  -webkit-filter: contrast(1.5) grayscale(100%);
}

/* .items:hover > *:not(:hover) {
  opacity: .9 !important;
} */

.square_overlay:hover {
  opacity: 1;
}

.square_overlay {
  display: inline-block;
  margin-top: 1.5em;
  width: calc((var(--site-width) - 4em) / 3);
  padding-top: 95%;
  height: 0;
  background-size: cover !important;
  cursor: pointer;
  background: var(--bright);
  /* opacity:0; */
}

.relative {
  position: relative;
}

.square_overlays {
  position: absolute;
  top: 0;
}

.items {
  display: flex;
  align-items: center;
  justify-content: space-between;
  -moz-column-gap: 1em;
  -webkit-column-gap: 1em;
  column-gap: 1em;
  height: auto;
  flex-wrap: wrap;
}

#middlebar div{
 margin:0;
}
#middlebar {
 display:flex;
 justify-content:space-between;
 align-items:center;
}

@media screen and (max-width: 1000px) {
  .h-flex {
    display: block;
  }

  .square_overlay {
    width: calc(85vw);
  }

  .item {
    width: calc(85vw);
  }
  .content,
  .description {
    width: 90%;
    margin: 0 5%;
  }
}
</style>
