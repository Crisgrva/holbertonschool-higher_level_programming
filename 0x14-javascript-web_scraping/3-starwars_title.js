#!/usr/bin/node
// Script that prints the title of Star Wars movie
const request = require('request');
const process = require('process');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.error('error: ', error);
  }
  body = JSON.parse(body);
  console.log(body.title);
});
