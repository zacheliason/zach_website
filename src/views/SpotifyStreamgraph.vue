<template>
  <div class="spotify">
    <div class="top-spacer"></div>
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
