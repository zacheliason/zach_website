<template lang="html">
  <div>
    <div class="top-spacer"></div>

    <h2>projects</h2>
	<ul style="list-style-type: none;padding:0">
        <li v-for="project in projects" :key="project.id">
          <router-link :to="'/projects/' + project.name">{{project.name.replaceAll("_", " ").replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase())}}<span class='date'> {{ format_date(project.date) }}</span></router-link>
        </li>
      <li><router-link to="/projects/spotify_streamgraph">Spotify Streamgraph Generator<span class='date'> 1/30/2021</span></router-link></li>
	</ul>
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
      return this.$root.$data.projects.filter(x => {
        return (!x.name.startsWith("HIDE"));
      });
    }
  }
}
</script>

<style lang="css" scoped>
.date {
  color: var(--dark);
  font-size: .7em;
  font-weight: bolder;
  font-family: 'ibm-plex-mono', mono;
}

a:hover {
  text-decoration: underline;
  border-bottom: 2px dotted var(--bright);
}

li a {
 color: black;
}

li::before {
  content: "# ";
  color: var(--dark);
}


</style>
