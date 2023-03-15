#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let hght = 0; hght < this.height; hght++) {
      console.log('X'.repeat(this.width));
    }
  }
};
