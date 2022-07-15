const cjson = require('compressed-json')
var fs = require('fs');
var CryptoJS = require("crypto-js");

let rawdata = fs.readFileSync('recipes.json');
let recipes = JSON.parse(rawdata);


var ciphertext = CryptoJS.AES.encrypt(JSON.stringify(recipes), 'zacheliason').toString()
const compressed = cjson.compress.toString(ciphertext)

fs.writeFile("ZACHENCRYPT.txt", compressed, function(err) {
    if (err) {
        console.log(err);
    }
});

