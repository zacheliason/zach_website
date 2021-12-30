<template lang="html">
  <div>
    <div class="top-spacer"></div>

    <h2>projects</h2>
    <div class="left">
      <div v-for="project in projects" :key="project.id">
        <li>
          <router-link :to="'/projects/' + project.name">{{project.name.replaceAll("_", " ").replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase())}}<span class='date'> {{ format_date(project.date) }}</span></router-link>
        </li>
      </div>
    </div>
    <div class="right">

    </div>
    <div class="top-spacer"></div>
  </div>
</template>

<script>
export default {
  name: "Projects",
  components: {
  },
  methods: {
    format_date(d) {
      let date = d.split('T')[0]
      let parts = date.split("-")
      return parts[1] + "/" + parts[2] + "/" + parts[0]
    },
  },
  computed: {
    projects() {
      return this.$root.$data.projects
    }
  }
}
</script>

<style lang="css" scoped>
.date {
  color: #b5b5b5;
  font-size: .7em;
  font-weight: bolder;
  font-family: 'ibm-plex-mono', mono;
}

a:hover {
  text-decoration: underline;
}

</style>
