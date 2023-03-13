#!/usr/bin/node
const argv = process.argv;
const size = parseInt(argv[2]);
const character= 'X'
if (isNaN(size)){
  console.log('Missing size');
}
else{
  for (let i = 1; i <= size; i++){
    console.log(character.repeat(size));
  }
}

