#!/usr/bin/node
// Create class Square that inherits from Rectangle
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    this.print(c);
  }
};
