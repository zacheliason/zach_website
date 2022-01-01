<template lang="html">
  <div>
    <div class="mobile">
      <div class="">
        <p>This app does not work on mobile. Please try a computer.</p>
        <router-link to="/">[home]</router-link>

      </div>
    </div>

    <div class="frontpage" v-if="front_page">
      <h2>request spotify data</h2>
      <p>First, request your data from Spotify at the bottom of your account's <a target="_blank" href="https://www.spotify.com/us/account/privacy/">Privacy Settings</a> page.
         (it may take up to 30 days to gather your streaming history) You will receive an email once it is ready to download. Then, click <a class="bold" v-on:click="change_page">here.</a> </p>
       <p>For an explanation of this project and its process, click <router-link to="/projects/spotify_streamgraph_explanation">here.</router-link>
 </p>
    </div>
    <div class="backpage" v-if="!front_page">

      <div class="import_data" v-if="import_pending">
          <h2>import spotify data</h2>
          <p>Your zipped data file will include a number of <span class='mono'>StreamingHistoryJSON</span> files starting from <span class='mono'>0</span> and counting up. Add each of these files sequentially, then press create to view your streamgraph.<br></p>
          <p><a class="bold" @click="change_page">[how to download spotify data]</a></p>
          <hr>
        <div class="left">
          <div class="box">
            <input @change="change_file" type="file" id="selectFiles" value="Import"><br>
            <label for="selectFiles" @change="change_file">select file</label>
            <button disabled :style="hover_style(file_selected)" id="import" @click="import_file();change_file();change_file_added();">{{import_text}}</button>
            <button id="gogogo" :style="hover_style(file_added)" @click="group_by_artist">create</button>
            <h2>files imported:</h2>
            <div v-for="file in files">
              <p class='mono'>{{file}}</p>
            </div>

          </div>
        </div>
      </div>

      <div class="vizpage" id="vizpage" v-bind:style=" import_pending ? 'display: none;' : 'display: unset;' ">

        <h2>top artists</h2>
        <div class="top-artists">
          <div class='top-artist' v-for="i in 20">
            {{i}}. <span class='bold mono'>{{top_artists[i - 1]}}:</span>
            {{minutes_to_hours(top_artists[i - 1])}}
          </div>
        </div>

        <div class="top-spacer"></div>

        <h2>streamgraph</h2>
        <!-- <div class="button1" v-on:click="changeCardinal">Cardinal</div>
        <div class="button1" v-on:click="changeStep">Step</div>
        <div class="button1" v-on:click="changePoint">Point</div> -->
        <!-- <button type="button" id="buttonXlim" >UP</button>
        <button class="downloadButton" @click="downloadWithCSS">Download PDF</button> -->
        <div v-bind:style=" cardinal_switch1 ? 'display: unset;' : 'display: none;' " id="streamgraph"></div>
        <div v-bind:style=" step_switch1 ? 'display: unset;' : 'display: none;' " id="streamgraph2"></div>
        <div v-bind:style=" point_switch1 ? 'display: unset;' : 'display: none;' " id="streamgraph3"></div>
        <button type="button" name="button" class="revert_button" @click="revert">reset</button>
      </div>
    </div>
    <div class="top-spacer">

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
      import_pending: true,
      demo_page: true,
      file_selected: false,
      front_page: true,
      cardinal_switch: true,
      step_switch: false,
      point_switch: false,
      import_text: "add file",
      file_added: false,
      fileNum: 0,
      temp_array: [],
      buttonHov: {
        color: 'white',
        backgroundcolor: '#f74825',
      },
    }
  },
  methods: {
    minutes_to_hours(artist) {
      let min = this.$root.$data.top_artists_keys[artist]

      var hours = Math.floor(parseInt(min) / 60);
      var minutes = parseInt(min) % 60;

     return hours + " hrs, " + minutes + " min"
    },
    revert() {
      this.file_added = false;
      this.demo_page = false;
      this.front_page = false;
      this.fileNum = 0;
      this.import_text = "add file";
      this.import_pending = true;
      this.$root.$data.importedJSON = [];
      this.$root.$data.artist_list = [];
      this.$root.$data.csv = '';
      this.$root.$data.top_artists = [];
      this.$root.$data.top_artists_keys = {};
      this.$root.$data.week_max = 0;
      this.$root.$data.new_width = 0;
      this.$root.$data.files_imported = [];

      let oldEl = document.getElementById('streamgraph');
      oldEl.remove();
      let newEl = document.createElement("div");
      newEl.id = "streamgraph";
      newEl.style.marginTop = "100px";
      document.getElementById("vizpage").appendChild(newEl);

    },
    changeDemo() {
      this.demo_page = !this.demo_page;
      this.front_page = !this.front_page;
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
    hover_style(watchedVar) {
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
        '--button-color--hover': this.buttonHov.backgroundcolor,
        '--button-background-color--hover': this.buttonHov.color,
        '--button-transition--hover': this.buttonHov.transition
      };
    },
    change_file() {
      this.file_selected = !this.file_selected;
      document.getElementById("import").disabled = !document.getElementById("import").disabled;
    },
    change_page() {
      this.front_page = !this.front_page;
    },
    change_file_added() {
      this.file_added = true;
      this.fileNum += 1;
      this.import_text = this.file_added ? 'add another' : 'add another';
    },
    changeCardinal() {
      this.cardinal_switch = true;
      this.step_switch = false;
      this.point_switch = false;
    },
    changeStep() {
      this.cardinal_switch = false;
      this.step_switch = true;
      this.point_switch = false;
    },
    changePoint() {
      this.cardinal_switch = false;
      this.step_switch = false;
      this.point_switch = true;
    },
    import_file() {
      var files = document.getElementById('selectFiles').files;
      if (files.length <= 0) {
        return false;
      }

      var fr = new FileReader();
      fr.fileName = files[0].name // file came from a input file element. file = el.files[0];

      fr.onload = e => {
        var result = JSON.parse(e.target.result);
        if (this.file_added == false) {
          this.$root.$data.importedJSON = result;
        } else if (this.file_added) {
          this.$root.$data.importedJSON = this.$root.$data.importedJSON.concat(result);
        }

        this.$root.$data.files_imported.push(e.target.fileName)
      }
      fr.readAsText(files.item(0))
    },
    group_by_artist() {
      this.$root.$data.jsonSuccess = true;
      let json = this.$root.$data.importedJSON;
      this.$root.$data.artist_list = _.mapValues(_.groupBy(json, "artistName"), x => x.map(y => _.omit(y, "artistName")));
      this.sumPlayTime();

    },
    sumPlayTime() {
      let artists = this.$root.$data.artist_list;
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
      let newNewArray = newArray.map(x => x.artistName + " " + x.minutesListened + " minutes listened")
      let coolobj = {}
      for (let i = 0; i < 20; i++) {
        this.$root.$data.top_artists.push(newArray[i].artistName)
        coolobj[newArray[i].artistName] = newArray[i].minutesListened.toFixed(2)
        this.$root.$data.top_artists_keys = coolobj
      }

      //this.$root.$data.artist_list
      this.jsonToCSV();
    },
    jsonToCSV() {
      let itemsList = this.$root.$data.importedJSON;
      let items = []
      let topArtistList = this.$root.$data.top_artists;
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
      this.$root.$data.week_max = maxListenTime;
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
      let brand_new_Array = []
      let brand_new_Obj = []
      let top_artists = this.$root.$data.top_artists;
      let weekObj = fooObj;
      // adds missing artists
      for (let week in weekObj) {
        let results = weekObj[week];
        for (let i in top_artists) {
          let topArtist = top_artists[i];
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
        brand_new_Obj = {}
        let results = weekObj[week];
        for (let i in results) {
          let artistObj = results[i];
          let artist = Object.keys(artistObj)[0];
          brand_new_Obj[artist] = artistObj[artist];
        }
        brand_new_Obj["week"] = week;
        brand_new_Array.push(brand_new_Obj)
        //brand_new_Obj
      }

      return brand_new_Array;
    },
    createStreamgraph() {
      let week_max = .7 * this.$root.$data.week_max;
      let csvToUse = this.$root.$data.csv;
      let topartistskeys = this.$root.$data.top_artists_keys
      var margin = {
          top: 20,
          right: 0,
          bottom: 30,
          left: 0,
        },

        width = 1220 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;
      this.$root.$data.new_width = width;

      // append the svg object to the body of the page
      var svg = d3.select("#streamgraph")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom + 100)
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
          .style("stroke", "black"))
        .call(g => g.selectAll(".tick line")
          .style("stroke", "black"))
        .call(g => g.selectAll(".tick text")
          .style("fill", "black")
          .style("font-family", "ibm-plex-mono"))
        .call(g => g.selectAll("text")
          .attr("transform", function(d) {
              return "rotate(45 -15 15)"
          }));


      svg.append("text")
        .attr("text-anchor", "end")
        .attr("x", width)
        .attr("y", height - 30)


      // Add Y axis
      var y = d3.scaleLinear()
        .domain([-week_max, week_max])
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
        .style("color", "#000000")
        .style("fill", "#000000")
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
        .style("color", "#000000")
        .style("fill", "#000000")
        .style("z-index", 10000)

      // Three function that change the tooltip when user hover / move / leave a cell
      var mouseover = function() {
        Tooltip.style("opacity", 1)
        Tooltip2.style("opacity", 1)
        d3.selectAll(".myArea").transition().duration(250).style("opacity", .2)
        d3.select(this)
          .transition().duration(151)
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

      this.import_pending = false;
      //this.createStreamgraphBlock();
      //this.createStreamgraphSharp();



    },
  },
  computed: {
    top_artists_keys() {
      return this.$root.$data.top_artists_keys
    },
    top_artists() {
      return this.$root.$data.top_artists
    },
    files() {
      return this.$root.$data.files_imported;
    },
    cardinal_switch1() {
      return this.cardinal_switch;
    },
    step_switch1() {
      return this.step_switch;
    },
    point_switch1() {
      return this.point_switch;
    }
  },
};
</script>


<style lang="css" scoped>

.left {
  height: 100%;
  display: flex;
  justify-content: flex-start;

}
.right {
  height: 100%;
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

.backpage {
  flex-wrap: nowrap;
  z-index: 999 !important;
  display: flex;
}
h1 {
  transition: .5s;
}
p {
  mix-blend-mode: unset !important;
}
.bold {
  color:#f74825;
}
a {
  text-decoration: none;
  color:#f74825;
  font-family: "ibm-plex-mono", mono;
  transition: .3s;
}
.tooltip text{
  color: black !important;
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
  font-family: 'ibm-plex-mono', mono;
  cursor: pointer;
  width: max-content;
  margin: 1em 1em 1em 0;
  display: block;
  padding: .3em 1em;
  border-style: solid;
  border-width: 3px;
  border-color: black;
  border-radius: 1000px;
  color: black;
}

label:hover{
  color:#f74825;
}

a:hover {
  mix-blend-mode: difference;
}

text {
  color: black;
  background-color: purple;
}
#buttonXlim {
  position: fixed;
  bottom: 30px;
  right: 30px;
}
.demo_page {
  background-color: black;
  height: auto;
  width: 100vw;
  z-index: 100;
  position: absolute;
  top: 0;
  left: 0;
}

.revert_button:hover {
  color: #f74825;
}

#streamgraph {
  display: flex;
  justify-content: center;
  height: 100%;
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
  color: black;
}

.mobile {
  display: none;
}

.revert_button {
  z-index: 9999999 !important;
  width: auto;
}

img {
  border: 0 !important;
}

.import_data {
  width: 100%;
}

.top-artists {
max-height: 15em;  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: flex-start;
  flex-direction: column;
}

.top-artist {
  width: 45%;
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
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top:0;
    left:0;
    text-align: center;
  }
  .mobile p {
    padding: 2em;
  }
}

</style>
