#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], ({ encoding: 'utf-8' }), function (err, data) {
  if (err) console.log(err);
  if (data) console.log(data);
});
