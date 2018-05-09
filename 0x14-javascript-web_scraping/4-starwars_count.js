#!/usr/bin/node

const request = require('request');
let url = process.argv[2];
let wedge = 'https://swapi.co/api/people/18/';
let wedg = 'http://swapi.co/api/people/18/';
let count = 0;

request(url, function (error, res, body) {
  if (error) console.log(error);
  let movies = JSON.parse(body).results;
  for (let i = 0; i < movies.length; i++) {
    if (movies[i].characters.includes(wedge) || movies[i].characters.includes(wedg)) {
      count++;
    }
  }
  console.log(count);
});
