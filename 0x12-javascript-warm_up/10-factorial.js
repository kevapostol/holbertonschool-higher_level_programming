#!/usr/bin/node
/*
Computes and prints a factorial
*/
let num = process.argv[2];
num = Number(num);

if (isNaN(num) === true) {
  num = 1;
}

console.log(factorial(num));

function factorial (n) {
  /*
  Factorial function
  */

  if (n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}
