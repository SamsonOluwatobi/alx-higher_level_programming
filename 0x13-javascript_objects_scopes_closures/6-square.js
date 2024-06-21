#!/usr/bin/node
/*  Base class to declare a Square with:
    - Specific size.
    - Validated dimensions.
    - Method to print representation in console
    (optionally using a specific character).
    - Method to swap the height and the width.
    - Method to double the dimensions of the Rectangle (multiplies by 2).
*/

const Base_square = require('./5-square');

class Square extends Base_square {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
