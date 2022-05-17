#!/usr/bin/node
const argv = process.argv;
const axios = require('axios').default;
const apii = 'https://swapi-api.hbtn.io/api/films/'.concat(argv[2])
axios.get(apii)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(error.response.status);
  });
