#!/usr/bin/node
let a = Number(process.argv[2]);
let b = Number(process.argv[3]);
if (a && b) {
  console.log(a + b);
} else {
  console.log(NaN);
}
