#!/usr/bin/node
const { argv } = require('process');
const newArray = [];
Array.from(argv).slice(2).forEach(element =>
  newArray.push(parseInt(element)));

console.log(newArray.sort(
  function (a, b) { return a - b; })[newArray.length - 2]);
