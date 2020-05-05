#!/usr/bin/node
/*
Prints a message depending of the number of arguments passed
*/
if (process.argv.length <= 1) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
