#!/usr/bin/node
/*
Prints My number: <first argument converted in integer> if the first argument
can be converted to an integer
*/
let num = process.argv[2];
num = parseInt(num);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
