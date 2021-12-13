#!/usr/bin/node
const { argv } = require('process');
const numbers = Array.from(argv).slice(2).sort();
const lstNum = numbers[numbers.length - 2];
argv.length > 3 ? console.log(lstNum) : console.log('0');
