#!/usr/bin/node

/*
writes string to a file
*/
const fs = require('fs');
const content = process.argv[3];
try {
  fs.writeFileSync(process.argv[2], content);
} catch (err) {
  console.log(err);
}
