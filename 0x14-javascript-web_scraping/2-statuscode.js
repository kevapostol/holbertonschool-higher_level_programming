#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
