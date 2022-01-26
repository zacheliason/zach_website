<template>
  <div id="app">
    <div id="bar">
      <div id="bar-container">
        <div >
            <router-link to="/"><h3>zacheliason{{pathname}}</h3></router-link>
        </div>
        <div id="right-box">
            <div class="">
              <router-link to="/projects">🤖 projects</router-link>
            </div>

            <div class="">
              <router-link to="/design">💿 design</router-link>
            </div>

            <div class="">
              <router-link to="/about">🙇‍♂️ about</router-link>
            </div>

        </div>

      </div>
    </div>

    <div style="height: calc(100vh - 3em);width:85%;margin: 0 auto;">
      <!-- VIEW ROUTER -->
      <router-view />
    </div>

    <footer>
      <div >
        <a target='_blank' href="https://www.instagram.com/z.eliason/">instagram</a>
      </div>
      <div >
        <a target='_blank' href="https://twitter.com/zachs_not_here">twitter</a>
      </div>
      <div >
        <a target='_blank' href="https://github.com/zacheliason/">github</a>
      </div>
      <div id='sitecode'>
        <a target='_blank' href="https://github.com/zacheliason/zach_website">[site code]</a>
      </div>
    </footer>

  </div>
</template>
<script type="text/javascript">
export default {
  name: "App",
  computed: {
    pathname() {
      let path = this.$route.path;
      path = path.replace('projects', '🤖')
      path = path.replace('design', '💿')
      path = path.replace('about', '🙇‍♂️')
      return path;
    }
  }
}

</script>
<style>

h3, h1, h2, h4, h5, h6 {
  font-family: ibm-plex-mono, monol;
}

a:hover {
  color:#f74825;
}

.smallcaps {
  font-variant: small-caps;
}

footer {
  font-size: .8em;
  font-family: ibm-plex-mono, mono;
  position: fixed;
  bottom: 0;
  display: flex;
  width: calc(100% - 15%);
  justify-content: space-between;
  z-index: 9999 !important;
  height: 3em;
  margin: 0 7.5%;
  text-align: center;
  mix-blend-mode: difference;
}

footer a {
  color: #4a4a4a;
  mix-blend-mode: difference;
}

footer a:hover {
  color: #08b7da;
}

p {
  font-family: ibm-plex-serif, serif;
  font-style: normal;
  font-weight: 100;
}

body {
  background-color: white;
  font-family: ibm-plex-sans, sans-serif;
  margin: 0;
}

a {
  text-decoration: none;
  color: black;
}

#bar-container {
  margin: 0 7.5%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

#bar {
  background: #ededed;
  width: 100vw;
  height: 3em;
  display: flex;
  color: black;
  z-index: 10;
  font-family: ibm-plex-mono, mono;
}

.left {
  width: 42%;
  height: calc(100% - 3em);
  position: relative;
  left: 0;
  top: 0;
}

.right {
  margin-right: 7.5%;
  height: calc(100% - 3em);
  width: 42%;
  position: absolute;
  right: 0;
  top: 3em;
  z-index: -1;
}

.page {
  height: 100%;
}

.top-spacer {
  height: 7.5vw;
}

.v-flex {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.h-flex {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

#right-box {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  width: 50%;

}

.invisible {
  opacity: 0;
}

.not-on-mobile {
  display: none;
}

.mono {
  font-family: 'ibm-plex-mono'; 
}

@media screen and (max-width: 820px) {
}

@media screen and (max-width: 620px) {
  #bar {
    height: unset;
    background: #ededed;
    padding-bottom: 1em;
  }

  #bar-container {
    margin: 0 7.5%;
    width: 100%;
    display: block;
  }

  #right-box {
    display: block;
  }

  .left {
    width: 100%;
    display: block;
    position: static;
  }


  .right {
    width: 100%;
    display: block;
    position: static;
  }

  #sitecode {
    display: none;
  }

  .bottom-spacer {
    height: 20vw;
  }

  .on_mobile {
    display: block;
  }

  .not_on_mobile {
    display: none;
  }
}
</style>
