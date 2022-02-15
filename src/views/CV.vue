<template>
  <div class="cv">
    <div class="top-spacer"></div>
    <vue-pdf-embed class="pdf" source="/cv_small.pdf" />
    <div class="top-spacer bottom-spacer"></div>
  </div>
</template>

<script>
import VuePdfEmbed from "vue-pdf-embed/dist/vue2-pdf-embed";

export default {
  components: {
    VuePdfEmbed
  }
};
</script>

<style media="screen" scoped>
.cv {
  background-color: var(--grey);
  position: absolute;
  left: 0;
  padding: 0 calc((100vw - var(--site-width)) / 2);
}

@media screen and (max-width: 620px) {
  .cv {
    width: 100%;
    padding: 0;
    position: unset;
    background-color: unset;
  }
  #router-view {
    background-color: var(--grey);
  }
}
</style>
