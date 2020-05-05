#!/usr/bin/node
/*
Prints a square
*/
let num = process.argv[2];
num = parseInt(num);

if (isNaN(num)) {
  console.log('Missing size');
}

for (let i = 0; i < num; i += 1) {
  for (let j = 0; j < num; j += 1) {
    process.stdout.write('X');
  }
  console.log();
}
