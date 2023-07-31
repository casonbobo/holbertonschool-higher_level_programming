#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      process.exit(0);
    this.width = w;
    this.height = h;
    }
  }
}
module.exports = Rectangle;
