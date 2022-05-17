#!/usr/local/bin/node

const axios = require('axios').default;
const argv = process.argv;
const apii = argv[2];
const path = argv[3];
const fs = require('fs');
axios.get(apii)
  .then(function (response) {
    fs.writeFile(path, response.data, 'utf8', function (err, data) {
      if (err) {
        console.error(err);
      }
      // file written successfully
    });
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
