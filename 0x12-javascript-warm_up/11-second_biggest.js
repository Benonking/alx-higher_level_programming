#!/usr/bin/node
const argv = process.argv.slice(2);
function secondMax (arrayArgs) {
  if (arrayArgs.length < 2) {
    return (0);
  } else {
    arrayArgs.sort((a, b) => a - b);
    arrayArgs.pop();
    return (arrayArgs.pop());
  }
}
console.log(secondMax(argv));
