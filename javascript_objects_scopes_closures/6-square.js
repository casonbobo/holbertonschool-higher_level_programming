#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    let char = '';
    if (c) {
        char += c;
    } else {
        char += 'X';
    }
    for (let i = 0; i < this.size; i++) {
        console.log(char);
    }
  }
}

module.exports = Square;
