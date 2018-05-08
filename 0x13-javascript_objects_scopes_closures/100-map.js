#!/usr/bin/node
// Import a list and multiply value at each index by the index
const list = require('./100-data.js').list;
let newList = list.map((value, idx) => value * idx);
console.log(list);
console.log(newList);
