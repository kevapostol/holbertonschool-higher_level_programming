#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newArr = list.map((x, idx) => x * idx);
console.log(newArr);
