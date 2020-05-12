#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const uri = process.argv[2];
const fileName = process.argv[3];
request.get(uri, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(fileName, body, (err) => {
      if (err) { console.log(err); }
    });
  }
});
