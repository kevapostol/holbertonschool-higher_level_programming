#!/usr/bin/node
/*
Searches the second biggest integer in the list of arguments
*/
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let liNums = [];

  for (let i = 2; i < process.argv.length; i += 1) {
    liNums.push(parseInt(process.argv[i]));
  }

  liNums = liNums.sort((a, b) => b - a);
  console.log(liNums[1]);
}
