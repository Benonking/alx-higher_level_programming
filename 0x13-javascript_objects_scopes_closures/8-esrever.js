#!/usr/bin/node
exports.esrever = function (list) {
  let idx = 0;
  let length = list.length - 1;
  while (idx < length) {
    const temp = list[idx];
    list[idx] = list[length];
    list[length] = temp;
    idx++;
    length--;
  }
  return list;
};
