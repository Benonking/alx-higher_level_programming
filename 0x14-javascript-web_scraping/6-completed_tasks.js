#!/usr/bin/node
// compute number of tasks complted from paceholderapi
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    responseDic = {};
    const responseList = JSON.parse(body);
    for (let i; i < responseList.length; i++) {
      if (responseList[i].completed === true) {
        if (responseDic[responseList[i].userId] === undefined) {
          responseDic[responseList[i].userId] = 1;
        } else {
          responseDic[responseList[i].userId]++;
        }
      }
    }
    console.log(responseDic);
  }
});
