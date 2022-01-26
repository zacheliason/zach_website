<template>
  <div style="height:100%;width:100%;">

    <div class="top-spacer"></div>

    <div class="left">
      <div class="left-box">
        <img src="/images/zach_homepage_2.png" alt="">
      </div>
    </div>

    <div class='right'>
      <div class="right-box">
        <div>
            <h2>Hi, I'm Zach!</h2>
            <p>I'm an enthusiastic bioinformatics student studying at <span class='smallcaps'>BYU</span> (2023) with interests in genetics, epidemiology, and quantitative ecology.</p>
            <!--<h1>🌱 🏔 👨‍🔬 🤖 🦠 🧬 ‍❤️‍🔥</h1>-->
            <!-- 🤠🤖💻🕴🐸🌍🪐🌝🎹🚲🌊🎞🦠🧬❤️‍🔥🇺🇦💽📀💾👨‍💻👾🌱✨ -->
        </div>
      </div>
    </div>

    <div class="bottom-spacer"></div>

  </div>
</template>

<script>
export default {
  name: "Home",
  components: {},
}
</script>

<style lang="css" scoped>
img {
  width: 100%;
}

.left-box {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.right-box {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

p {
  font-family: 'ibm-plex-sans', sans-sans-serif;
}

.top-spacer {
  height: 0;
}
@media screen and (max-width: 820px) {

}

@media screen and (max-width: 620px) {
  .left-box {
    height: unset;
  }

  h1 {
    font-size: 1.8em;
  }

  .left, .right {
    height: unset;
  }

  .right-box {
    height: unset;
    display: block;
    align-items: center;
  }
}
</style>
