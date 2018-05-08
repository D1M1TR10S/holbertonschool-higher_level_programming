#!/usr/bin/node
// Create class Rectangle
// with methods that alter
// width and height

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print (chr='X') {
    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
