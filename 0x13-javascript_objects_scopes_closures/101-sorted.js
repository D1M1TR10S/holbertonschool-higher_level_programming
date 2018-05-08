#!/usr/bin/node
// Import a list and multiply value at each index by the index
const dct = require('./101-data.js').dict;
let d = {}

for (var key in dct) {
  let data = dct[key];
  console.log("data: " + data);
  if (!d[data.key]) {
    d[data.key] = [];
  }
  console.log("data.val: " + data.val)
  d[data.key].push(key);
}
console.log(d);
