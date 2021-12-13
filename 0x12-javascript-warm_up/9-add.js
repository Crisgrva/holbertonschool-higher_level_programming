#!/usr/bin/node
const { argv } = require('process');
const fstNum = parseInt(argv[2]);
const scndNum = parseInt(argv[3]);

function add (a, b) {
  return a + b;
}
console.log(add(fstNum, scndNum));
