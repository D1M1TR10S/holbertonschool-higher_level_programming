#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
let wedge = 'https://swapi.co/api/people/18/';

request(url, function (error, res, body) {
  if (!error) {}
  let movies = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < movies.length; i++) {
    if (movies[i].characters.indexOf(wedge) > -1) {
      count++;
    }
  }
  console.log(count);
});
