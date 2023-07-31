#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
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
