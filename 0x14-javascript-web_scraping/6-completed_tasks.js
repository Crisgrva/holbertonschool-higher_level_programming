#!/usr/bin/node
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
  for (const user of body) { persons[user.userId] = []; }

  for (const user of body) {
    if (user.completed === true) {
      persons[String(user.userId)].push(user.id);
    }
  }

  const newDict = {};
  for (const [key, value] of Object.entries(persons)) {
    newDict[key] = value.length;
  }
  console.log(newDict);
});
