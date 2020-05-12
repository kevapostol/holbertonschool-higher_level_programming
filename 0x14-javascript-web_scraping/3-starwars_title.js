#!/usr/bin/node
const request = require('request');
const uri = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
request.get(uri, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
