#!/usr/bin/node
let arr = process.argv.slice(2).map(Number).sort().reverse();
if (arr.length >= 2) {
  console.log(arr[1]);
} else {
  console.log(0);
}
