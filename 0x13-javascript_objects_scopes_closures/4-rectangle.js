#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const str = 'X'.repeat(this.width);
      console.log(str);
    }
  }

  rotate () {
    for (let i = 0; i < this.width; i++) {
      const str = 'X'.repeat(this.height);
      console.log(str);
    }
  }

  double () {
    for (let i = 0; i < this.height; i++) {
      const str = 'X'.repeat(this.width * 2);
      console.log(str);
    }
  }
}

module.exports = Rectangle;
