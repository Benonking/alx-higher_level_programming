#!/usr/bin/node
// compute number of tasks complted from paceholderapi
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const responseDic = {};
    const responseList = JSON.parse(body);
    for (let i = 0; i < responseList.length; i++) {
      if (responseList[i].completed === true) {
        if (responseList[i].userId in responseDic) {
          responseDic[responseList[i].userId] += 1;
        } else {
          responseDic[responseList[i].userId] = 1;
        }
      }
    }
    console.log(responseDic);
  }
});
