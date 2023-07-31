#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w <= 0 || h <= 0) {
      process.exit(0);
    }
  }

  print () {
    let xCount = 0;
    let yCount = 0;
    let output = '';
    for (; xCount < this.width; xCount++) {
      output += 'X';
    }
    for (; yCount < this.height; yCount++) {
      console.log(output);
    }
  }
}
module.exports = Rectangle;
