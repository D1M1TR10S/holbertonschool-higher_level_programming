#!/usr/bin/node
let size = Number(process.argv[2]);
let i = 0;
if (size) {
  for (i; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
