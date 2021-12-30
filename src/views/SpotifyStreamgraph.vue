<template>
  <div class="spotify">
    <FileImport />
  </div>
</template>

<script>
// @ is an alias to /src
import FileImport from "@/components/FileImport.vue";

export default {
  name: "SpotifyStreamgraph",
  components: {
    FileImport
  }
};
</script>

<style media="screen">
  .spotify {
    z-index: 9999999999999999 !important;
    position: absolute;
  }
</style>
