#!/usr/bin/node
/*  Base class to declare a Square with:
    - Specific size.
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);// Call the constructor of Rectangle with size for both width and height
  }
}

module.exports = Square;
