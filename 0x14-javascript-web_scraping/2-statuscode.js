#!/usr/bin/node

const req = require('axios');

req.get(process.argv[1])
    .then(function (response) {
        console.log(response.statusCode);
    })
    .catch(function (error) {
        console.log(error);
    });