let fs = require('fs')

let rawdata = fs.readFileSync('recipes.json');
let recipes = JSON.stringify(JSON.parse(rawdata));

function ceasar(string, shift) {
  let resultArray = []
  for (let i = 0; i < string.length; i++) {
    let code = string.charCodeAt(i) + shift
    resultArray.push(String.fromCharCode(code))
  }
  return resultArray.join("")
}

let compressed = ceasar(recipes, 1)
//compressed = ceasar(compressed, -1)

fs.writeFile("new.txt", compressed, function(err) {
    if (err) {
        console.log(err);
    }
});

