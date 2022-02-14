<template>
<div id="project-viewer" style="margin:0 auto">
    <div class="top-spacer"></div>

    <h2 style='color: var(--bright);display:inline-block;margin-bottom: 0;padding-right: .3em;'>{{ remove_underscores($route.params.id) }}</h2>
  
    |
    <div class="date">
      posted {{ this.date }}

    </div>
    <hr>
    <vue-markdown id='markdown' :source="md">
    </vue-markdown>

    <hr>
    <div class="flexbox">

      <div class='v-flex' v-if="if_previous_project">
        <p class='no-padding sans'>newer projects</p>
        <div class="break"></div>
        <h6 class='no-padding'><router-link :to="'/projects/' + previous_project.name"><- {{ remove_underscores(previous_project.name) }}</router-link></h6>
      </div><div v-else></div>

      <div class='v-flex' style='justify-content:right;' v-if="if_next_project">
        <p class='no-padding sans'>older projects</p>
        <div class="break"></div>
        <h6 class='no-padding'><router-link :to="'/projects/' + next_project.name">{{ remove_underscores(next_project.name) }} -></router-link></h6>
      </div>

    </div>

    <div class="top-spacer bottom-spacer"></div>
</div>
</template>

<script>
import Prism from 'prismjs'
// import 'prismjs-darcula-theme/darcula.css';
// import '../assets/darcula.css'
import '../assets/material.css'
import 'prismjs/components/prism-bash'
import 'prismjs/components/prism-javascript'
import 'prismjs/components/prism-python'
import 'prismjs/components/prism-r'

export default {
  name: "ProjectViewer",
  props: {
  },
  mounted() {
    Prism.highlightAll()
  },
  methods: {
    remove_underscores(word) {
      return word.replaceAll("_", " ").replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase())
    }
  },
  computed: {
    if_previous_project() {
      let projects = this.$root.$data.projects
      let new_index = this.project_index - 1
      if (new_index >= 0) {
        return true
      } else {
        return false
      }
    },
    if_both() {
      return this.if_next_project && this.if_previous_project
    },
    if_next_project() {
      let projects = this.$root.$data.projects
      let new_index = this.project_index + 1
      if (new_index < projects.length) {
        return true
      } else {
        return false
      }
    },
    previous_project() {
      let projects = this.$root.$data.projects
      let new_index = this.project_index - 1
        return projects[new_index]
    },
    next_project() {
      let projects = this.$root.$data.projects
      let new_index = this.project_index + 1
        return projects[new_index]
    },
    project_index() {
      let projects = this.$root.$data.projects
      let name = this.$route.params.id

      var i = projects.findIndex(function(post, index) {
      	if(post.name == name)
      		return true;
      });
      return i

    },
    project() {
      let projects = this.$root.$data.projects
      return projects[this.project_index]
    },
    date() {
      let date = this.project.date.split('T')[0]
      let parts = date.split("-")
      return parts[1] + "/" + parts[2] + "/" + parts[0]
    },
    md() {
      let project = this.project
      let contents = project.contents
      contents = contents.replace(/!\[(.*?)\]\((.+?)\)/, '![]($2)<p class="alt">$1</p>')

      return contents
    }
  },
  data() {
    return {}
  },
}
</script>


<style type="text/css">
h1,h2,h3,h4,h5,h6 {
  font-family: ibm-plex-mono, mono;
}

#project-viewer a {
 color: var(--dark);
 border-bottom: dotted 2px var(--dark);
}

#project-viewer a:hover  {
  color: #73838b;
  border-bottom: dotted 2px #73838b;
}

h3 {
  font-family: 'ibm-plex-mono', mono;
}

li {
  line-height: 2em;
}

#project-viewer img {
  width: 100%;
}

.date {
  display: inline;
  padding: 0 .3em;
  color: var(--dark);
  font-size: .7em;
  font-weight: bolder;
  font-family: 'ibm-plex-mono', mono;
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
  height: .3em;
}

.no-padding {
  padding: 0;
  margin: 0;
}

.sans {
  font-family: 'ibm-plex-sans', sans-serif;
  color: var(--dark);
  font-size: .7em;
}

#markdown {
  min-height: 50vh;
}

@media screen and (max-width: 820px) {

}

@media screen and (max-width: 620px) {
  #markdown {
    min-height:
  }


  pre {
    overflow: scroll;
  }

}

</style>
