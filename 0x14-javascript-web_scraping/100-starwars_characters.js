#!/usr/bin/node
// print all characters of a starwars movie
const request = require('request');
const ID = process.argv[2];
const url = 'https://swapi.co/api/films/' + ID;

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const charList = JSON.parse(body).characters;
    for (let j = 0; j < charList.length; j++) {
      request.get(charList[j], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
