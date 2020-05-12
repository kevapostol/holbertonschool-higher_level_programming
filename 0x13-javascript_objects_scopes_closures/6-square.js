#!/usr/bin/node
const SquareP = require('./5-square');
module.exports = class Square extends SquareP {
  charPrint (C) {
    if (C === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(C.repeat(this.width));
      }
    }
  }
};
