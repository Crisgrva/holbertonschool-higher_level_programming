#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);

function Factorial (number) {
  if (number === 0 || !number) { return 1; }
  return (number * Factorial(number - 1));
}

console.log(Factorial(number));
