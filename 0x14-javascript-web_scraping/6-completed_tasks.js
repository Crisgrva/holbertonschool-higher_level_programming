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
  // Creating all users
  for (const user of body) { persons[user.userId] = 0; }

  for (const user of body) {
    if (user.completed === true) {
      persons[String(user.userId)]++;
    }
  }
  console.log(persons);
});
