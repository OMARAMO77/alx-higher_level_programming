#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (character) {
    if (!character) {
      character = 'X';
    }
    this.print(character);
  }
}

module.exports = Square;
