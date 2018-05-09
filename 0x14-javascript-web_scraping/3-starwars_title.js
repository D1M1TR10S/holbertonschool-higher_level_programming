#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2].toString();
request(url, function (error, res, body) {
  if (!error) {
    let obj = JSON.parse(body);
    console.log(obj.title);
  }
});
