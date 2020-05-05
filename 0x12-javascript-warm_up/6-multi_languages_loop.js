#!/usr/bin/node
/*
Prints 3 lines: (like 1-multi_languages.js) but by using an array of string and
a loop
*/
const arrStr = [
  'C is fun',
  'Python is cool',
  'Javascript is amazing'
];

for (let i = 0; i < arrStr.length; i += 1) {
  console.log(arrStr[i]);
}
