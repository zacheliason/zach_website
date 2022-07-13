<template>
  <div class='home-box'>
      <div>
      <div class='top-spacer'></div>
      <div class="left-box">
      <!--<img style='max-width: 10em;' src="/images/ZachProfile3.png" alt="" />-->
      </div>
      <div class="right-box">
        <div style="height:100%;">
          <h1 class='home-header'>Zach Eliason</h1>
          <p class='home-text'>
            I am a student studying bioinformatics at
            <span class="smallcaps">BYU</span> (2023). <br>
            I am interested in computational cancer immunology and genomics research. I also have experience in ecology and statistics research.
          </p>

          <!--<h1>🌱 🏔 👨‍🔬 🤖 🦠 🧬 ‍❤️‍🔥</h1>-->
          <!-- 🤠🤖💻🕴🐸🌍🪐🌝🎹🚲🌊🎞🦠🧬❤️‍🔥🇺🇦💽📀💾👨‍💻👾🌱✨ -->
        </div>
      </div>
    <div class="bottom-spacer"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  components: {}
};
</script>

<style lang="css" scoped>
img {
  width: 100%;
  padding: 0;
}

p {
  font-family: "ibm-plex-sans", sans-sans-serif;
}

.box {
  display: flex;
  justify-content: space-between;
}

.home-header {
  font-weight: 800;
  font-size: 3em;
}

.home-text {
  font-size: 2em;
  font-weight: 800;
}

.home-box {
  height:100%;
  width:100%;
  display:flex;
  align-items:center;
}

@media screen and (max-width: 820px) {
}

@media screen and (max-width: 620px) {
  .home-box {
    height: unset;
    display: unset;
  }

  .home-header {
    font-size:2em;
  }

  .home-text {
    font-size: 1.5em;
  }

  .box {
    flex-wrap: wrap;
  }

  h1 {
    font-size: 1.8em;
  }

  .left,
  .right {
    height: unset;
  }

  .right-box {
    height: unset;
    display: block;
    align-items: center;
    margin-left: unset;
  }

  .top-spacer {
    height: 7.5vw;
  }

  .left-box {
    flex: unset;
    margin-right: unset;
    margin-bottom: 7.5vw;
    height: unset;
  }
}
</style>
