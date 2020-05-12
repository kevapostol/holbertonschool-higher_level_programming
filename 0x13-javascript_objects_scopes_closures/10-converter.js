#!/usr/bin/node
exports.converter = function (base) {
  return (number) => parseInt(number, 10).toString(base);
};
