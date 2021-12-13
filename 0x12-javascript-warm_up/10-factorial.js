#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);
let total = 1;

for (let i = 1; i <= number; i++) {
  total *= i;
}

console.log(total);
