#!/usr/bin/node
/*
Prints the addition of 2 integers
*/
const num1 = process.argv[2];
const num2 = process.argv[3];
add(num1, num2);

function add (a, b) {
  const num1 = Number(a);
  const num2 = Number(b);

  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
  } else {
    console.log(num1 + num2);
  }
}
