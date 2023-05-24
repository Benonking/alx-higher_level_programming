#!/usr/bin/node
// compute number of tasks complted from paceholderapi
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const responseList = JSON.parse(body);
    for (let i; i < responseList.length; i++) {
      if (responseList[i].completed === true) {
        console.log(responseList);
      }
    }
  }
});
