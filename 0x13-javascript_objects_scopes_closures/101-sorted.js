#!/usr/bin/node
const dict = require('./101-data').dict;
const obj = {};

for (const [key, val] of Object.entries(dict)) {
  if ((val in obj) === false) {
    obj[val] = [key];
  } else {
    obj[val].push(key);
  }
}
console.log(obj);
