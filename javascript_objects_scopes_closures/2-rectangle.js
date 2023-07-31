#!/usr/bin/node
class rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w <= 0 || h <= 0) {
      process.exit (0);
    }
  }
}
module.exports = rectangle;
