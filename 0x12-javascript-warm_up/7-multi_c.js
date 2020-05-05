#!/usr/bin/node
/*
Prints x times “C is fun"
*/
let num = process.argv[2];
num = parseInt(num);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < num; i += 1) {
  console.log('C is fun');
}
