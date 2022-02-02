#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const persons = {};

  body = JSON.parse(body);
  for (const user of body) {
    if (user.completed) {
      if (persons[user.userId] === undefined) {
        persons[user.userId] = 0;
      } else {
        persons[user.userId]++;
      }
    }
  }
  console.log(persons);
});
