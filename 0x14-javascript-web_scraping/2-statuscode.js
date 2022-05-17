#!/usr/bin/node

/*
This is a module
that does something
*/
const argv = process.argv;
const axios = require('axios').default;

axios.get(argv[2])
    .then(function (response) {
        console.log('code: ' + response.statusCode);
    })
    .catch(function (error) {
        console.log('code: ' + error.response.status);
    });