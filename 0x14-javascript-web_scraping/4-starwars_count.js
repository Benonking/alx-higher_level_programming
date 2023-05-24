#!/usr/bin/node
// print number of movies where the character "Wadge Antiilles" is present
const request = require('request');
const url = process.argv[2];

function filmCharacterCount (url) {
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      let count = 0;
      const ID = /18/;
      const response = JSON.parse(body).results;
      for (let i = 0; i < response.length; i++) {
        const charList = response[i].characters;
        for (let f = 0; f < charList.length; f++) {
          if (ID.test(charList[f]) === true) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
filmCharacterCount(url);
