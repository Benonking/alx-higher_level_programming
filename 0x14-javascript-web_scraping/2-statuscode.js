#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
let response = fetch(req);
request(url, function (error, response, body){
    if (error) throw error;
    console.log('code: ', response.statusCode);
});