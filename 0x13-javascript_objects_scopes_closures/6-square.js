#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        const str = c.repeat(this.width);
        console.log(str);
      }
    }
  }
}

module.exports = Square;
