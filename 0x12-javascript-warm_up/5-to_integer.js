#!/usr/bin/node
const { argv } = require('process');
(parseInt(argv[2])) ? console.log(`My number: ${argv[2]}`) : console.log('Not a number');
