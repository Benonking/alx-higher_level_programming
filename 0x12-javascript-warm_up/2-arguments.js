#!/usr/bin/node
const index = process.argv.length;
console.log(index === 2 ? 'No argument' : index === 3 ? 'Argument found' : 'Arguments found');
