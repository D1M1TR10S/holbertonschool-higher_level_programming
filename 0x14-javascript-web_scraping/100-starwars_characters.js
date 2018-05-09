#!/usr/bin/node
const request = require('request');

let url = 'http://swapi.co/api/films/' + process.argv[2].toString();
let dct = {};
let ordered = {};

request(url, function (error, result, body) {
  if (!error) {
    let chrs = JSON.parse(body).characters;
    
    for (let i = 0; i < chrs.length; i++) {
      request(chrs[i], function (err, res, bod) {
        if (!err) {
          let name = JSON.parse(bod).name;
          let key = JSON.parse(bod).url;
          dct[key] = name;
          
          if (i == chrs.length - 1) {
            chrs.forEach(function(key) {
                console.log(dct[key]);
            });
          }
        }
      });
    }
  }
});
