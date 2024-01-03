#!/usr/bin/node
const request = require('request');

const path = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(path, function (err, response, body) {
  if (err) console.log(err);
  if (body) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
