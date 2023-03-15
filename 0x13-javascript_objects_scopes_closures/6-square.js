#!/usr/bin/node
const Ss = require('./5-square');
module.exports = class Square extends Ss {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let size = 0; size < this.width; size++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
