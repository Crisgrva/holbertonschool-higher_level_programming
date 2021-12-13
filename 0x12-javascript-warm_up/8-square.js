#!/usr/bin/node
const { argv } = require('process');

if (parseInt(argv[2])) {
  const times = parseInt(argv[2]);

  for (let i = 0; i < times; i++) {
    console.log('X'.repeat(times));
  }
} else {
  console.log('Missing size');
}
