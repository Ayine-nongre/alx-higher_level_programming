#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  if (body) {
    fs.writeFile(process.argv[3], body, ({ encoding: 'utf-8' }), (err) => {
      if (err) console.log(err);
    });
  }
});
