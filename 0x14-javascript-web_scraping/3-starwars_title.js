#!/usr/bin/node
// print title of star wars movie if the episode number matches
const { error } = require('console');
const request = require('request');
const id = process.argv[2];
const endpoinUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(endpoinUrl, function (err, response, body) {
  if (err) throw error;
  console.log(JSON.parse(body).title);
});
