<template>
  <div style="height:100%;width:100%;">

    <div class="top-spacer"></div>
    <div class="box">
      <div class="left-box">
        <img src="/images/zach_homepage_2.png" alt="">
      </div>
      <div class="right-box">
        <div style="height:100%;">
            <h2 style="margin-top:0;">Hi, I'm Zach!</h2>
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
.top-spacer {
  height: 30%;
}

img {
  width: 100%;
  padding:0;
}

.left-box {
  display: flex;
  justify-content: center;
  align-items: center;
  flex:1;
  margin-right:1em;
}

.right-box {
  display: flex;
  justify-content: center;
  align-items: center;
  flex:1;
  margin-left:1em;
}

p {
  font-family: 'ibm-plex-sans', sans-sans-serif;
}

.box {
  display:flex;
  justify-content: space-between;
}

@media screen and (max-width: 820px) {

}

@media screen and (max-width: 620px) {
  .box {
    flex-wrap: wrap;
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
    margin-left: unset;
  }

  .top-spacer {
    height: 7.5vw;
  }

  .left-box {
    flex:unset;
    margin-right:unset;
    margin-bottom: 7.5vw;
    height: unset;
  }

}
</style>
