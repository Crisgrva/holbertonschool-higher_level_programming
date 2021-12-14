#!/usr/bin/node
module.exports =
  class Square extends require('./5-square') {
    constructor (size) {
      super(size, size);
    }
    charPrint (c) {
      c = c ? c : 'X';
      for (let i = 0; i < this.height;i++) {
        console.log(c.repeat(this.width));
      }
    }
};
