#!/usr/bin/node
let string = 'C is fun';
let times = Number(process.argv[2]);
let i = 0;
if (times) {
  for (i; i < times; i++) {
    console.log(string);
  }
} else {
  console.log('Missing number of occurrences');
}
