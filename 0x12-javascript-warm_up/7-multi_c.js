#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (!isNaN(n)) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
