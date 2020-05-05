#!/usr/bin/node
/*
Searches the second biggest integer in the list of arguments
*/
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let li_nums = [];

  for (let i = 2; i < process.argv.length; i += 1) {
    li_nums.push(parseInt(process.argv[i]));
  }

  li_nums = li_nums.sort((a, b) => b - a);
  console.log(li_nums[1]);
}
