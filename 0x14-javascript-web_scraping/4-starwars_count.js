#!/usr/bin/node
// Script that prints the number of movies where the character
// “Wedge Antilles” is present.
const request = require('request');
const process = require('process');

const url = process.argv[2];
const characterUrl = /(18)/g;

let counter = 0;

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(counter);
    return;
  }
  body = JSON.parse(body);
  for (const movie of body.results) {
    if (movie.characters.some(e => characterUrl.test(e))) {
      counter++;
    }
  }
  console.log(counter);
});
