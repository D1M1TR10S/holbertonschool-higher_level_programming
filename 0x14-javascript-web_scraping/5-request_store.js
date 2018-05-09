#!/usr/bin/node

const request = require('request');
const fs = require('fs');
let file = process.argv[3];
let url = process.argv[2];

request(url, function (error, res, body) {
  if (error) console.log(error);
  fs.writeFile(file, body, 'utf8', function (err, data) {
    if (err) {
      return console.log(err);
    }
  });
});
