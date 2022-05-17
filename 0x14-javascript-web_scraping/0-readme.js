#!/usr/local/opt/node@10/bin/node

/*
  Exercise 14: Web Scraping
  this does some stuff and
  then prints it out
*/
fs = require('fs')
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err)
  } else {
    console.log(data)
  }
});
