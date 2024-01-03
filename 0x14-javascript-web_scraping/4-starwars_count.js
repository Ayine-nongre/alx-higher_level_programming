#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  if (body) {
    const data = JSON.parse(body).results;
    let count = 0;

    for (const result of data) {
      for (const character of result.characters) {
        if (character.endsWith('/18/')) count++;
      }
    }
    console.log(count);
  }
});
