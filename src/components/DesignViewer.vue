<template>
  <div style="height:100%;">

    <div class="content">
      <div class="flex-content">
        <div class="image-wrap" style="padding-top:7.5vw"></div>
        <div v-for="image in images" :key="image" class="image-wrap">
          <img :src="'/images/' + image" alt="" />
        </div>
        <div class="top-spacer"></div>
      </div>
      <div class="description">
        <h2 class="item-header">{{ item_name }}</h2>
        <div class="date">
          {{ item_date }}
        </div>

        <hr />
        <p>{{ item_description }}</p>
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
    item_index() {
      let items = this.$root.$data.items;
      let name = this.$route.params.id;

      var i = items.findIndex(function(post, index) {
        if (post.name == name) return true;
      });
      return i;
    },
    item() {
      let items = this.$root.$data.items;
      return items[this.item_index];
    },
    images() {
      let item = this.item;
      return item.image;
    },
    item_name() {
      return this.item.name;
    },
    item_description() {
      return this.item.description;
    },
    item_date() {
      return this.item.date;
    }
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style lang="css" scoped>
.item-header {
  display: inline-block;
  margin-bottom: 0;
  padding-right: 0.3em;
}

#left-box {
  height: 100%;
}

img {
  padding: 0 0 1em 0;
  /*max-height: var(--site-width);*/
  max-height: 95vh;
  max-width: 80vw;
}

.date {
  display: inline;
  padding: 0 0.3em;
  color: var(--dark);
  font-size: 0.7em;
  font-weight: bolder;
  font-family: "ibm-plex-mono", mono;
}

.date::before {
  /*content:'|';*/
  content: "published ";
  color: black;
  font-size: 1em;
}

.content {
  position: absolute;
  width: 80vw;
  margin: 0 10vw;
  left: 0;
}

.flex-content {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}

.image-wrap {
  width: var(--site-width);
  display: flex;
  justify-content:center;
  margin-bottom:1em;
}

.description {
  flex: 1;
  width: var(--site-width);
  margin: 0 auto;
}

@media screen and (max-width: 1000px) {
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
  .item-header {
    max-width: 90vw;
    overflow-x: hidden;
  }
}
</style>
