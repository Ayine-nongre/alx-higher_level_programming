#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    const str = 'X'.repeat(n);
    console.log(str);
  }
}
