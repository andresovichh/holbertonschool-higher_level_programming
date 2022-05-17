#!/usr/bin/node
const argv = process.argv;
const axios = require('axios').default;
const apii = (argv[2]);
axios.get(apii)
  .then(function (response) {
    let counter = 0;

    for (const film in response.data.results) {
      if (response.data.results[film].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        counter = counter + 1;
      }
    }
    console.log(counter);
  })
  .catch(function (error) {
    error = 0;
    console.log(error);
  });
