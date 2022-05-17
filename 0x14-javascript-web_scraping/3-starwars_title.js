#!/usr/bin/node
const axios = require('axios').default;
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/')
  .then(function (response) {
    console.log('code: ' + response.data.title);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
