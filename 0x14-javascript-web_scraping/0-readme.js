#!/usr/bin/node
// read and print content of a file

const fileName = process.argv[2];
const fs = require('fs');

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
