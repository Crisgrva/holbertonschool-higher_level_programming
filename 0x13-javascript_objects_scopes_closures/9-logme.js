#!/usr/bin/node
class counter {
  static globalCounter = 0;
  constructor(){
    this.counter = counter.globalCounter;
    counter.globalCounter++;
  }
}
exports.logMe = function (item) {
  let tmp = new counter()
  console.log( `${tmp.counter}: ${item}`);
};
