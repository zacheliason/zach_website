<template>
  <div id="app">
    <div id="bar">
      <div id="bar-container">
        <div>
          <router-link to="/" class="bar-h3"
            ><h3>zacheliason{{ pathname }}</h3></router-link
          >
        </div>
        <div id="right-box">
          <div
            @mouseover="emoji('projects')"
            @mouseleave="leaveemoji('projects')"
          >
            <router-link to="/projects" id="emoji-projects" class="emoji"
              >🤖</router-link
            >
          </div>

          <div @mouseover="emoji('design')" @mouseleave="leaveemoji('design')">
            <router-link to="/design" class="emoji" id="emoji-design"
              >💿</router-link
            >
          </div>

          <div @mouseover="emoji('about')" @mouseleave="leaveemoji('about')">
            <router-link to="/about" class="emoji" id="emoji-about"
              >🙇‍♂️
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <div id="mobile-bar">
      <div id="bar-container">
        <div>
          <router-link to="/" class="bar-h3"
            ><h3>zacheliason{{ pathname }}</h3></router-link
          >
        </div>

        <div id="right-box">
          <div class="">
            <router-link class="mono" to="/projects">🤖 projects</router-link>
          </div>

          <div class="">
            <router-link class="mono" to="/design">💿 design</router-link>
          </div>

          <div class="">
            <router-link class="mono" to="/about">🙇‍♂️ about</router-link>
          </div>
        </div>
      </div>
    </div>

    <!--<div style="margin:0 auto;position:absolute;top:3.5em;border-bottom: 3px dotted black; width:30vw"></div>-->
    <div id="router-view" style="height: calc(100vh - 3em);margin: 0 auto;">
      <!-- VIEW ROUTER -->
      <router-view />
    </div>

    <footer>
      <div>
        <a target="_blank" href="https://www.instagram.com/z.eliason/"
          >instagram</a
        >
      </div>
      <div>
        <a target="_blank" href="https://twitter.com/zachs_not_here">twitter</a>
      </div>
      <div>
        <a target="_blank" href="https://github.com/zacheliason/">github</a>
      </div>
      <div id="sitecode">
        <a target="_blank" href="https://github.com/zacheliason/zach_website"
          >[site code]</a
        >
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
      path = path.replace("projects", "🤖");
      path = path.replace("design", "💿");
      path = path.replace("about", "🙇‍♂️");
      path = path.replace("HIDE_", "");

      if (this.isMobile()) {
        return "";
      } else {
        return path;
      }
    }
  },
  methods: {
    isMobile() {
      let check = false;
      (function(a) {
        if (
          /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(
            a
          ) ||
          /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(
            a.substr(0, 4)
          )
        )
          check = true;
      })(navigator.userAgent || navigator.vendor || window.opera);
      return check;
    },
    async emoji(key) {
      var el = document.getElementById("emoji-" + key);
      var temp = el.innerHTML;
      if (temp.indexOf(key) == -1) {
        el.innerHTML = el.innerHTML + " " + key;
      }
    },
    leaveemoji(key) {
      var el = document.getElementById("emoji-" + key);
      if (el.innerHTML.indexOf(key) != -1)
        el.innerHTML = el.innerHTML.split(" " + key)[0];
    }
  }
};
</script>
<style>
:root {
  --site-width: 50vw;
  --grey: #fafafa;
  --dark: #90a4ae;
  --bright: #f74825;
  /*--bright: #f6a434;*/
}

* {
  box-sizing: border-box;
}

.mono {
  font-family: ibm-plex-mono, mono;
}

#app {
  width: var(--site-width);
  margin: 0 auto;
}

h3,
h1,
h2,
h4,
h5,
h6 {
  font-family: ibm-plex-mono, monol;
}

a:not(.emoji):hover {
  text-decoration: none;
  color: var(--bright);
}

.smallcaps {
  font-variant: small-caps;
}

footer {
  font-size: 0.8em;
  font-family: ibm-plex-mono, mono;
  position: fixed;
  bottom: 0;
  display: flex;
  justify-content: space-between;
  z-index: 9999 !important;
  height: 3em;
  text-align: center;
  mix-blend-mode: difference;
  width: var(--site-width);
  margin: 0 auto;
}

footer a {
  color: #6f5b51;
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
  text-decoration: none !important;
  color: var(--dark);
}

#bar-container {
  margin: 0 auto;
  width: var(--site-width);
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: var(--dark);
}

#bar {
  position: absolute;
  top: 0;
  left: 0;
  background: var(--grey);
  width: 100vw;
  height: 3em;
  margin: 0 auto;
  display: flex;
  z-index: 10;
  font-family: ibm-plex-mono, mono;
}

.left {
  width: calc(20vw);
  height: calc(100% - 3em);
  position: relative;
  left: 0;
  top: 0;
}

.right {
  margin-right: calc(var(--site-width) / 2);
  height: calc(100% - 3em);
  width: calc(var(--site-width) / 2);
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
  width: var(--width);
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
}

.invisible {
  opacity: 0;
}

.not-on-mobile {
  display: none;
}

.mono {
  font-family: "ibm-plex-mono";
}

.emoji a:hover {
  color: var(--dark) !important;
}

.emoji {
  padding: 0.55em 0.5em;
  margin: 0 0.1em;
  /*border-radius: .4em;*/
  font-size: 1.17em;
}

.emoji-text {
  display: none;
  width: 0;
  overflow: hidden;
}

#mobile-bar {
  display: none;
  height: 0;
}

.large {
  width: 80vw !important;
  margin: 0 10vw;
  position: absolute;
  left: 0;
}

@media screen and (max-width: 1000px) {
  .large {
    width: 100% !important;
    margin: unset;
    position: unset;
    left: unset;
  }

  #router-view {
    padding: 5%;
  }

  #app {
    width: 100vw;
  }

  #mobile-bar {
    display: block;
    height: unset;
    background: var(--grey);
    padding: 1em 0;
  }

  #bar {
    display: none;
  }

  #bar-container {
    margin: 0 5%;
    width: 90%;
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

  footer {
    width: 90vw;
    margin: 0 5vw;
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
  body {
    overflow-x: hidden;
    margin: 0;
    padding: 0;
    width: 100vw;
  }

  #mobile-bar h3 {
    margin-top: 0;
  }
}
</style>
