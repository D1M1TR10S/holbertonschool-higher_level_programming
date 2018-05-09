#!/usr/bin/node
const request = require('request');

let url = 'http://swapi.co/api/films/' + process.argv[2].toString();

request(url, function (error, result, body) {
  if (!error) {
    let chrs = JSON.parse(body).characters;
    for (let i = 0; i < chrs.length; i++) {
      request(chrs[i], function (err, res, bod) {
        if (!err) {
          let name = JSON.parse(bod).name;
          console.log(name);
        }
      });
    }
  }
});
