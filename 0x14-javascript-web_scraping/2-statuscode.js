#!/usr/bin/node

const req = require('axios');
const argv = process.argv;
req.get(argv[2])
    .then(function (response) {
        console.log('code' + response.statusCode);
    })
    .catch(function (error) {
        console.log(error);
    });