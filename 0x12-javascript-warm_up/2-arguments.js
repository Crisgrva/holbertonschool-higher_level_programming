#!/usr/local/bin/node
const { argv } = require('process');

const lenght = argv.length - 2;
if (lenght === 0) {
  console.log('No argument');
} else if (lenght === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
