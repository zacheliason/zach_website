<template>
  <div id="project-viewer" style="margin:0 auto">
    <div class="top-spacer"></div>
    <vue-markdown id="markdown" :source="md"></vue-markdown>
    <p>View my full cv <router-link class='mono' to="/about/cv">here</router-link>.</p>

    <hr />
    <div class="top-spacer bottom-spacer"></div>
  </div>
</template>

<script>
import Prism from "prismjs";
import "../assets/material.css";
import "prismjs/components/prism-bash";
import "prismjs/components/prism-javascript";
import "prismjs/components/prism-python";
import "prismjs/components/prism-r";

export default {
  name: "About",
  props: {},
  mounted() {
    Prism.highlightAll();
  },
  methods: {
  },
  computed: {
    project() {
      return this.$root.$data.about[0]
    },
    date() {
      let date = this.project.date.split("T")[0];
      let parts = date.split("-");
      return parts[1] + "/" + parts[2] + "/" + parts[0];
    },
    md() {
      let project = this.project;
      let contents = project.contents;
      contents = contents.replace(
        /!\[(.*?)\]\((.+?)\)/,
        '![]($2)<p class="alt">$1</p>'
      );
      contents = contents.replace(
        /\[(.*?)\]\(([^\.]*?)\)/,
        '[$1](https://zacheliason.com/#/projects/$2)'
      );
      console.log(contents)

      return contents;
    }
  },
  data() {
    return {};
  }
};
</script>

<style type="text/css">
h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: ibm-plex-mono, mono;
}

#project-viewer a {
  color: var(--dark);
  border-bottom: dotted 2px var(--dark);
}

#project-viewer a:hover {
  color: #73838b;
  border-bottom: dotted 2px #73838b;
}

h3 {
  font-family: "ibm-plex-mono", mono;
}

li {
  line-height: 2em;
}

#project-viewer img {
  width: 100%;
}

.date {
  display: inline;
  padding: 0 0.3em;
  color: var(--dark);
  font-size: 0.7em;
  font-weight: bolder;
  font-family: "ibm-plex-mono", mono;
}

.inline {
  display: inline-block;
}

.flexbox {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.break {
  flex-basis: 100%;
  height: 0.3em;
}

.no-padding {
  padding: 0;
  margin: 0;
}

.sans {
  font-family: "ibm-plex-sans", sans-serif;
  color: var(--dark);
  font-size: 0.7em;
}

#markdown {
  min-height: unset;
}

@media screen and (max-width: 820px) {
}

@media screen and (max-width: 620px) {
  #markdown {
    min-height: unset;
  }

  pre {
    overflow: scroll;
  }
}
</style>
