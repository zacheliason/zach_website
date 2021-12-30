<template>
<div style='height:100%;'>
  <div class="top-spacer"></div>

  <div class="right">
  <div class="top-spacer"></div>
  <h2 class='invisible'>spacer</h2>
  <hr class='invisible'>
    <div v-for="image in images" :key="image">
      <img :src="'/images/' + image" alt="">
    </div>
    <div class="top-spacer"></div>
  </div>

  <div class="left" id='left-box'>
    <h2 style='display:inline-block;margin-bottom: 0;padding-right: .3em;'>{{ item_name }}</h2>
    <div class="date">
      {{ item_date }}

    </div>

    <hr>
    <p>{{item_description}}</p>
    <div class="top-spacer"></div>
  </div>


</div>
</template>

<script>
export default {
  name: "DesignViewer",
  props: {
  },
  computed: {
    item_index() {
      let items = this.$root.$data.items
      let name = this.$route.params.id

      var i = items.findIndex(function(post, index) {
        if(post.name == name)
          return true;
      });
      return i

    },
    item() {
      let items = this.$root.$data.items
      return items[this.item_index]
    },
    images() {
      let item = this.item
      return item.image
    },
    item_name() {
      return this.item.name
    },
    item_description() {
      return this.item.description
    },
    item_date() {
      return this.item.date
    },
  },
  data() {
    return {}
  },
  methods: {
  }
}
</script>


<style lang="css" scoped>
#left-box {
  height: 100%;
}

img {
  padding: 0 0 1em 0;
}

.date {
  display: inline;
  padding: 0 .3em;
  color: #b5b5b5;
  font-size: .7em;
  font-weight: bolder;
  font-family: 'ibm-plex-mono', mono;
}

.date::before {
  content:'|';
  color: black;
  font-size: 1em;
}


@media screen and (max-width: 820px) {

}

@media screen and (max-width: 620px) {
  .right {
    height:unset;
  }

  #left-box {
    height:unset;
    padding-bottom: 20vw;
  }

  .date::before {
    content:unset;
    color: black;
    font-size: 1em;
  }

}

</style>
