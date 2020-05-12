#!/usr/bin/node

if (process.argv.length !== 5) {
  console.error('Incorrect number of Args');
} else {
  // Reading the files
  const fs = require('fs');
  const targetFile = process.argv[4];
  let newStr = '';
  newStr += fs.readFileSync(process.argv[2]);
  newStr += fs.readFileSync(process.argv[3]);

  // Writing the file
  fs.writeFile(targetFile, newStr, (err) => {
    if (err) console.log(err);
  });
}
