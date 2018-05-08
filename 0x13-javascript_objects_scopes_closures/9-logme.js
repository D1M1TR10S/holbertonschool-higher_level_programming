#!/usr/bin/node
// Prints the argument passed and counts how many times its called 

let count = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(count + ': ' + item);
    count++;
  }
};
