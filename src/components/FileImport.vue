<template lang="html">
  <div id="all">
    <router-link @click="revert" id="exit" to="/coding"> &#x2715;</router-link>
    <div class="mobile">
      <p>This app does not work on mobile. Please try a computer!</p>
    </div>
    <div class="frontpage" v-if="frontPage">
      <p>First, request your data from Spotify at the bottom of your account's <a target="_blank" href="https://www.spotify.com/us/account/privacy/">Privacy Settings</a> page.
         (it may take up to 30 days to gather your streaming history) You will receive an email once it is ready to download. Then, <span class="bold" v-on:click="changePage">click here.</span> </p>
    </div>
    <div class="backpage" v-if="!frontPage">

      <div class="importStuff" v-if="importPending">
        <div class="left">
          <div class="box">
            <input @change="changeFile" type="file" id="selectFiles" value="Import"><br>
            <label for="selectFiles" @change="changeFile">Select File</label>
            <button disabled :style="hoverStyle(fileSelected)" id="import" @click="importFile();changeFile();changeFileAdded();">{{importText}}</button>
            <button id="gogogo" :style="hoverStyle(fileAdded)" @click="groupByArtist">Create</button>
            <h1>Files added: {{fileNum}}</h1>
            <div class="dot-windmill"></div>
          </div>
        </div>
        <div class="right">
          <div class="box">
            <p>After you've unzipped your data file, you should see a number of <b> StreamingHistory </b> JSONs starting from 0 and counting up, depending on how much music you listened to. Add each of these files in order, then create your streamgraph.<br><br> <span class="bold" @click="changePage">Forgot how to get your Spotify data?</span> </p>
          </div>
        </div>
      </div>
      <div class="vizpage" id="vizpage" v-bind:style=" importPending ? 'display: none;' : 'display: unset;' ">
        <button type="button" name="button" class="revertButton" @click="revert">Reset</button>
        <!--<div class="button1" v-on:click="changeCardinal">Cardinal</div>
        <div class="button1" v-on:click="changeStep">Step</div>
        <div class="button1" v-on:click="changePoint">Point</div>
        <button type="button" id="buttonXlim" >UP</button>
        <button class="downloadButton" @click="downloadWithCSS">Download PDF</button>-->
        <div v-bind:style=" cardinalSwitch1 ? 'display: unset;' : 'display: none;' " id="my_dataviz"></div>
        <!--<div v-bind:style=" stepSwitch1 ? 'display: unset;' : 'display: none;' " id="my_dataviz2"></div>
        <div v-bind:style=" pointSwitch1 ? 'display: unset;' : 'display: none;' " id="my_dataviz3"></div>-->
      </div>
    </div>


  </div>
</template>

<script>
import _ from 'lodash';
import moment from 'moment';
import * as d3 from "d3";
//import * as html2canvas from 'html2canvas';
//import * as jsPDF from 'jspdf';
//import * as html2pdf from 'jspdf-html2canvas';

export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  data() {
    return {
      demoPage: true,
      fileSelected: false,
      frontPage: true,
      cardinalSwitch: true,
      stepSwitch: false,
      pointSwitch: false,
      importText: "Add File",
      fileAdded: false,
      fileNum: 0,
      tempArray: [],
      buttonHov: {
        backgroundcolor: 'white',
        color: 'black',
        transition: '.3s',
      },
    }
  },
  methods: {
    revert() {
      this.fileAdded = false;
      this.demoPage = false;
      this.frontPage = false;
      this.fileNum = 0;
      this.importText = "Add File";
      this.$root.$data.importPending = true;
      this.$root.$data.importedJSON = [];
      this.$root.$data.artistList = [];
      this.$root.$data.csv = '';
      this.$root.$data.topArtists = [];
      this.$root.$data.topArtistsKeys = {};
      this.$root.$data.weekMax = 0;
      this.$root.$data.newWidth = 0;
      let oldEl = document.getElementById('my_dataviz');
      oldEl.remove();
      let newEl = document.createElement("div");
      newEl.id = "my_dataviz";
      newEl.style.marginTop = "100px";
      document.getElementById("vizpage").appendChild(newEl);

    },
    changeDemo() {
      this.demoPage = !this.demoPage;
      this.frontPage = !this.frontPage;
    },
    downloadWithCSS() {
      let page = document.getElementById('all');
      var opt = {
        margin: 1,
        filename: 'myfile.pdf',
        image: {
          type: 'jpeg',
          quality: 0.98
        },
        html2canvas: {
          scale: 2
        },
        jsPDF: {
          unit: 'in',
          format: 'letter',
          orientation: 'portrait'
        }
      };
      html2pdf().set(opt).from(page).save();
      /*html2canvas(document.body).then(function(canvas) {
        var pdfHeight = window.screen.height;
        var pdfWidth = window.screen.width;
        var doc = new jsPDF('l','px',[pdfHeight,pdfWidth]);
        doc.appendChild(canvas);
        doc.save('test.pdf');
      });*/
    },
    hoverStyle(watchedVar) {
      if (!watchedVar) {
        return {
          '--button-opacity': .3,
          '--button-color--hover': this.buttonHov.backgroundcolor,
          '--button-background-color--hover': this.buttonHov.color,
          '--button-transition--hover': this.buttonHov.transition
        };
      }
      return {
        '--button-opacity': 1,
        '--button-color--hover': this.buttonHov.color,
        '--button-background-color--hover': this.buttonHov.backgroundcolor,
        '--button-transition--hover': this.buttonHov.transition
      };
    },
    changeFile() {
      this.fileSelected = !this.fileSelected;
      document.getElementById("import").disabled = !document.getElementById("import").disabled;
    },
    changePage() {
      this.frontPage = !this.frontPage;
    },
    changeFileAdded() {
      this.fileAdded = true;
      this.fileNum += 1;
      this.importText = this.fileAdded ? 'Add Another' : 'Add Another';
    },
    changeCardinal() {
      this.cardinalSwitch = true;
      this.stepSwitch = false;
      this.pointSwitch = false;
    },
    changeStep() {
      this.cardinalSwitch = false;
      this.stepSwitch = true;
      this.pointSwitch = false;
    },
    changePoint() {
      this.cardinalSwitch = false;
      this.stepSwitch = false;
      this.pointSwitch = true;
    },
    importFile() {
      var files = document.getElementById('selectFiles').files;
      if (files.length <= 0) {
        return false;
      }

      var fr = new FileReader();
      fr.onload = e => {
        var result = JSON.parse(e.target.result);
        if (this.fileAdded == false) {
          this.$root.$data.importedJSON = result;
        } else if (this.fileAdded) {
          this.$root.$data.importedJSON = this.$root.$data.importedJSON.concat(result);

        }
      }
      fr.readAsText(files.item(0))
    },
    groupByArtist() {
      this.$root.$data.jsonSuccess = true;
      let json = this.$root.$data.importedJSON;
      this.$root.$data.artistList = _.mapValues(_.groupBy(json, "artistName"), x => x.map(y => _.omit(y, "artistName")));
      this.sumPlayTime();

    },
    sumPlayTime() {
      let artists = this.$root.$data.artistList;
      let newArray = [];
      for (var artist in artists) {
        var tempSum = 0;
        for (var i in artists[artist]) {
          tempSum += parseInt(artists[artist][i].msPlayed, 10)
        }
        tempSum /= 60000
        let newObject = {
          artistName: artist,
          minutesListened: tempSum
        }
        newArray.push(newObject)
      }
      newArray.sort((a, b) => {
        return b.minutesListened - a.minutesListened;
      });
      console.log("Top 50 Artists");
      let newNewArray = newArray.map(x => x.artistName + " " + x.minutesListened + " minutes listened")
      for (let i = 1; i < 51; i++) {
        //console.log("Number " + i + " " + newNewArray[i]);
      }
      let coolobj = {}
      for (let i = 0; i < 20; i++) {
        this.$root.$data.topArtists.push(newArray[i].artistName)
        coolobj[newArray[i].artistName] = newArray[i].minutesListened.toFixed(2)
        this.$root.$data.topArtistsKeys = coolobj
      }

      //this.$root.$data.artistList
      this.jsonToCSV();
    },
    jsonToCSV() {
      let itemsList = this.$root.$data.importedJSON;
      let items = []
      let topArtistList = this.$root.$data.topArtists;
      for (let item in itemsList) {
        if (topArtistList.includes(itemsList[item].artistName)) {
          items.push(itemsList[item])
        }
      }
      let newItems = this.groupByWeek(items)
      let sumArray = []
      for (let i in newItems) {
        let sumWeek = 0;
        let tempArtist = newItems[i];
        for (let art in tempArtist) {
          let artistString = art;
          if (artistString != "week") {
            sumWeek += tempArtist[artistString];
          }
        }
        sumArray.push(sumWeek)
      }
      let maxListenTime = 0;
      for (let num in sumArray) {
        if (sumArray[num] > maxListenTime) {
          maxListenTime = sumArray[num]
        }
      }
      this.$root.$data.weekMax = maxListenTime;
      const replacer = (key, value) => value === null ? '' : value // specify how you want to handle null values here
      const header = Object.keys(newItems[0])
      const csv = [
        header.join(','), // header row first
        ...newItems.map(row => header.map(fieldName => JSON.stringify(row[fieldName], replacer)).join(','))
      ].join('\r\n')
      this.$root.$data.csv = csv;
      this.createStreamgraph();
    },
    groupByWeek(items) {
      //let arrayItems = []
      let objectItems = _.groupBy(items, (result) => moment(result['endTime'], 'YYYY-MM-DD HH:mm').startOf('isoWeek'));
      let newArray = []
      let weekArray = []
      let groupedWeekArray = []
      for (let item in objectItems) {
        weekArray = objectItems[item]
        groupedWeekArray = _.mapValues(_.groupBy(weekArray, "artistName"), x => x.map(y => _.omit(y, "artistName")));
        for (var artist in groupedWeekArray) {
          var tempSum = 0;
          for (var i in groupedWeekArray[artist]) {
            tempSum += parseInt(groupedWeekArray[artist][i].msPlayed, 10)
          }
          tempSum /= 60000
          let newObj = {}
          newObj[artist] = tempSum;
          newObj["week"] = item
          newArray.push(newObj)
        }
      }
      let groupedWeekObj = _.mapValues(_.groupBy(newArray, "week"), x => x.map(y => _.omit(y, "week")));

      let fixedArray = this.parseWeek(groupedWeekObj);
      return fixedArray;
    },
    parseWeek(fooObj) {
      let braveNewArray = []
      let braveNewObj = []
      let topArtists = this.$root.$data.topArtists;
      let weekObj = fooObj;
      // adds missing artists
      for (let week in weekObj) {
        let results = weekObj[week];
        for (let i in topArtists) {
          let topArtist = topArtists[i];
          var checkForArtist = results.some(obj => topArtist in obj);
          if (checkForArtist) {
            continue
          } else {
            let missingArtist = {};
            missingArtist[topArtist] = 0;
            results.push(missingArtist)
          }
        }
      }
      //consolidates weeks and artist play counts
      for (let week in weekObj) {
        braveNewObj = {}
        let results = weekObj[week];
        for (let i in results) {
          let artistObj = results[i];
          let artist = Object.keys(artistObj)[0];
          braveNewObj[artist] = artistObj[artist];
        }
        braveNewObj["week"] = week;
        braveNewArray.push(braveNewObj)
        //braveNewObj
      }

      return braveNewArray;
    },
    createStreamgraph() {
      let weekMax = .7 * this.$root.$data.weekMax;
      let csvToUse = this.$root.$data.csv;
      let topartistskeys = this.$root.$data.topArtistsKeys
      // set the dimensions and margins of the graph
      //if (window.innerWidth) console.log(window.innerWidth);
      //else console.log(920);
      var margin = {
          top: 20,
          right: 30,
          bottom: 30,
          left: 30
        },

        width = 920 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;
      this.$root.$data.newWidth = width;

      // append the svg object to the body of the page
      var svg = d3.select("#my_dataviz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

      // Parse the Data
      let data = d3.csvParse(csvToUse)
      // List of groups = header of the csv files
      var keys = data.columns
      keys.pop()

      // Add X axis
      var x = d3.scaleTime()
        .domain([new Date(data[0].week), new Date(data[data.length - 1].week)])
        .range([0, width]);

      var xAxis = svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x).ticks(data.length - 1))
        .call(g => g.select(".domain")
          .style("stroke", "white"))
        .call(g => g.selectAll(".tick line")
          .style("stroke", "white"))
        .call(g => g.selectAll(".tick text")
          .style("fill", "white")
          .style("font-family", "space mono"));

      //console.log(xAxis);
      svg.append("text")
        .attr("text-anchor", "end")
        .attr("x", width)
        .attr("y", height - 30)


      // Add Y axis
      var y = d3.scaleLinear()
        .domain([-weekMax, weekMax])
        .range([height, 0]);


      // color palette
      var color = d3.scaleOrdinal()
        .domain(keys)
        .range(["#aadedd", "#dc523f", "#de8735", "#4886af", "#92a488", "#4d5860",
          "#662d91", "#00a99d", "#ff7bac", "#d4145a", "#236a87", "#9e005d", "#29abe2",
          "#99815f", "#8cc63f", "#ffd3a0", "#bdc6bc", "#d9e021", "#c2a089", "#fdfdb8"
        ])

      //stack the data?
      var stackedData = d3.stack()
        .offset(d3.stackOffsetSilhouette)
        .keys(keys)
        (data)

      // create a tooltip
      var Tooltip = svg
        .append("text")
        .attr("class", "tooltip")
        .attr("x", 0)
        .attr("y", 0)
        .style("opacity", 0)
        .style("font-size", 17)
        .style("color", "#FFFFFF")
        .style("fill", "#FFFFFF")
        .style("font-weight", "bolder")
        .style("z-index", 10000)
        .style("mix-blend-mode", "difference")

      var Tooltip2 = svg
        .append("text")
        .attr("class", "tooltip")
        .attr("x", 0)
        .attr("y", 20)
        .style("opacity", 0)
        .style("font-size", 17)
        .style("color", "#FFFFFF")
        .style("fill", "#FFFFFF")
        .style("z-index", 10000)

      // Three function that change the tooltip when user hover / move / leave a cell
      var mouseover = function() {
        Tooltip.style("opacity", 1)
        Tooltip2.style("opacity", 1)
        d3.selectAll(".myArea").transition().duration(250).style("opacity", .2)
        d3.select(this)
          .transition().duration(151)
          .style("stroke", "black")
          .style("opacity", 1)
      }
      var grp = ""
      var grp2 = 0
      var mousemove = function(d) {
        grp = d.srcElement.__data__.key
        Tooltip.text(grp)

        grp2 = topartistskeys[grp]
        var hours = Math.floor(parseInt(grp2) / 60);
        var minutes = parseInt(grp2) % 60;


        Tooltip2.text(hours + " hours and " + minutes + " minutes listened")

      }
      var mouseleave = function() {
        Tooltip.style("opacity", 0)
        Tooltip2.style("opacity", 0)

        d3.selectAll(".myArea").transition().duration(151).style("opacity", 1).style("stroke", "none")
      }

      // Area generator
      var area = d3.area()
        .x(function(d) {
          return x(new Date(d.data.week));
        })
        .y0(function(d) {
          return y(d[0]);
        })
        .y1(function(d) {
          return y(d[1]);
        })
        .curve(d3.curveCardinal)

      // Show the areas

      svg
        .selectAll("mylayers")
        .data(stackedData)
        .enter()
        .append("path")
        .attr("class", "myArea")
        .style("fill", function(d) {
          return color(d.key);
        })
        .attr("d", area)
        .on("mouseover", mouseover)
        .on("mousemove", mousemove)
        .on("mouseleave", mouseleave)
        console.log("SVG: ");
        console.log(svg);
        console.log("AREA:");
        console.log(area);
      /*
        svg
        .selectAll("myCircles")
        .data(stackedData)
        .enter()
        .append("circle")
        .attr("fill", "blue")
        .attr("stroke", "none")
        .attr("cx", function(d) {
          return x(d.date)
        })
        .attr("cy", function(d) {
          return y(d.value)
        })
        .attr("r", 3)
      */
      function updatePlot() {
        /*
        x.domain([new Date(data[3].week), new Date(data[data.length - 3].week)]);
        svg.select(".x")
          .transition().duration(1500).ease("sin-in-out")
          .call(x);
        xAxis.transition().duration(1000).call(d3.axisBottom(x))
        */
        svg.selectAll("mylayers")
          .data(stackedData)
          .transition()
          .duration(1000)
          .append("path")
      }

      d3.select("#buttonXlim").on("click", updatePlot);

      this.$root.$data.importPending = false;
      //this.createStreamgraphBlock();
      //this.createStreamgraphSharp();



    },
  },
  computed: {
    importPending() {
      return this.$root.$data.importPending;
    },
    cardinalSwitch1() {
      return this.cardinalSwitch;
    },
    stepSwitch1() {
      return this.stepSwitch;
    },
    pointSwitch1() {
      return this.pointSwitch;
    }
  },
  mounted: function() {
    document.getElementById("all").classList.add('fade');
  }
};
</script>


<style lang="css" scoped>
* {
  font-family: 'Space Mono', monospace;
}
h2 {
  font-weight: normal !important;
}
.spotify {
}
#all {
    opacity: 1;
    transition-duration: 0.7s;
    transition-property: opacity;
    overflow: scroll;
  }

#all .fade {
  opacity: 0;
}
.left {
  position: absolute;
  left: 0;
  width: 50vw;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center !important;
  border-style: dotted;
  border-color: white;
  border-width: 0 3px 0 0;
}
.right {
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
  position: absolute;
  right: 0;
  width: 50vw;

}
.downloadButton {
  position: fixed;
  top: 30px;
  right: 30px;
}
button {
  flex: 100%;
  opacity: var(--button-opacity);
}
button:hover {
  color: var(--button-color--hover);
  background-color: var(--button-background-color--hover);
  border-transition: var(--button-transition--hover);
}

.frontpage {
  height: 100vh;
  width: 100vw;
  background-color: black;
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.backpage {
  flex-wrap: nowrap;
  height: 100vh;
  width: 100vw;
  background-color: black !important;
  z-index: 999 !important;
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
}
.importStuff {
  text-align: center;
}
h1 {
  color: white;
  transition: .5s;
  font-size: 2em;
}
p {
  font-family: "Space Mono", monospace !important;
  mix-blend-mode: unset !important;
}
.backpage p {
  text-align: center;
  color: white;
  font-size: 1.5em;
  margin: 0 20%;
}
.frontpage p {
  text-align: center;

  color: white;
  margin: 30px 10%;
  font-size: 2.5em;
}
.bold {
  font-weight: bolder;
  cursor: pointer;
  transition: .3s;
}
a {
  text-decoration: none;
  color: inherit;
  font-weight: bolder;
  transition: .3s;
}
.tooltip text{
  color: white !important;
  fill: red;
}
#selectFiles {
  width: 0.1px;
	height: 0.1px;
	opacity: 0;
	overflow: hidden;
	position: absolute;
	z-index: -1;
}
label,button {
  cursor: pointer;
  width: max-content;
  margin: 15px auto;
  display: block;
  padding: .3em 1em;
  border-style: solid;
  border-width: 3px;
  border-color: white;
  border-radius: 1000px;
  color: white;
  transition: .5s;
  font-size: 2em;
  background-color: black;
}
label:hover{
  background-color: white;
  color: black;
  transition: .3s;
}
a:hover,.bold:hover {
  transition: .3s;
  color: #24CFFA /*teal*/;
}
text {
  color: white;
  background-color: purple;
}
#buttonXlim {
  position: fixed;
  bottom: 30px;
  right: 30px;
}
.demoPage {
  background-color: black;
  text-align: center;
  height: auto;
  width: 100vw;
  z-index: 100;
  position: absolute;
  top: 0;
  left: 0;
}
.demoPage img {
  width: 80%;
}
.demoPage button:hover, .revertButton:hover {
  background-color: white;
  color: black;
  transition: .5s;
}
.demoPage button {
  margin-bottom: 60px;
}

.dot-windmill {
  margin: 0 auto;
  position: relative;
  top: -10px;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: yellow;
  color: yellow;
  transform-origin: 5px 15px;
  animation: dotWindmill 4s infinite linear;
  transform: scale(5);
  transition: 2s;

}

.dot-windmill::before, .dot-windmill::after {
  content: '';
  display: inline-block;
  position: absolute;
}

.dot-windmill::before {
  left: -8.66px;
  top: 15px;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: #5A00FF /*blue*/;
  color: #5A00FF /*blue*/;
}

.dot-windmill::after {
  left: 8.66px;
  top: 15px;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: #24CFFA /*teal*/;
  color: #24CFFA /*teal*/;
}
#my_dataviz {
  display: flex !important;
  align-items: center;
  justify-content: center;
  height: 100%;
  position: absolute;
  left: 100px;
  right: 0;
  top: 0;
}
@keyframes dotWindmill {
  0% {
    transform: rotateZ(0deg) translate3d(0, 0, 0);
  }
  100% {
    transform: rotateZ(720deg) translate3d(0, 0, 0);
  }
}
.fixme {
  position: fixed;
  bottom: 50px;
  right: 50px;
  color: white;
  font-size: 1em;
}
.mobile {
  display: none;
  font-size: .5em;
  padding: 30px;
}
.mobile p {
  color: white;
}

.revertButton {
  position: fixed;
  left: 50px;
  bottom: 50px;
  z-index: 9999999 !important;
  font-size: 1.5em;
  width: auto;
}

img {
  border: 0 !important;
}
#exit:hover{
  transform: scale(2);
  transition: .4s;
}
#exit {
  transform: rotate(0);
  transition: .3s;
  position: fixed;
  top: 30px;
  right: 50px;
  color: white;
  z-index: 99999999 !important;
  font-size: 2em;
}
h2  {
  padding: 0 20%;
  color: white;
}
@media screen and (max-width: 900px) {
  .frontpage,.backpage {
    height: 130vh;
  }
}
@media screen and (max-width: 620px) {
  .mobile {
    z-index: 99999 !important;
    height: 100vh;
    width: 100vw;
    background-color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    text-align: center;
  }
}

</style>
