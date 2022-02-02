#!/usr/bin/node
// Script that gets the contents of a
// webpage and stores it in a file.
const fs = require('fs');
const process = require('process');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) { console.error(error); return; }

  fs.writeFile(file, body, (err) => {
    if (err) { console.error(err); }
  });
});
