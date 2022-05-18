#!/usr/bin/node

/*
script that computes the number of
tasks completed by user id for each user
*/
const axios = require('axios').default;
const argv = process.argv;
const apii = argv[2];

axios.get(apii)
    .then(function (response) {
        const dict = {};
        /* console.log(response.data); */
        for (const x in response.data) {
            const user = response.data[x].userId;
            const ended = response.data[x].completed;
            if (isNaN(dict[user]) && ended) {
              dict[user] = 1;
            } else if (ended) {
              dict[user] += 1;
            }
          }
          console.log(dict);
        });