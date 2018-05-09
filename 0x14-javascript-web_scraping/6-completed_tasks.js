#!/usr/bin/node
const request = require('request');

let url = process.argv[2];
let dct = {};

request(url, function (error, res, body) {
  if (error) console.log(error);

  let lst = JSON.parse(body);
  for (let i = 0; i < lst.length; i++) {
    if (lst[i].completed === true) {
      if (lst[i].userId in dct) {
        dct[lst[i].userId]++;
      } else {
        dct[lst[i].userId.toString()] = 1;
      }
    }
  }
  console.log(dct);
});
