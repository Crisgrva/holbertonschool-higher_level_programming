#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:
const request = require('request');
const process = require('process');

const movieId = process.argv[2];
const movieUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

request.get(movieUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  body = JSON.parse(body).characters;
  body.forEach(element => {
    request.get(element, function (error, response, body) {
      if (error) { console.error(error); }
      console.log(JSON.parse(body).name);
    });
  });
});
