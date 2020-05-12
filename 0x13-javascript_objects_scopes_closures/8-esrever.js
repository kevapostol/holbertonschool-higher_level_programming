#!/usr/bin/node
exports.esrever = function (list) {
  let newList;
  for (let i = list.legth - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
