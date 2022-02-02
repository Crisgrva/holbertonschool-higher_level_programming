#!/usr/bin/node
// Script that display the status code of a GET request.
const request = require('request');
const process = require('process');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error: ', error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
