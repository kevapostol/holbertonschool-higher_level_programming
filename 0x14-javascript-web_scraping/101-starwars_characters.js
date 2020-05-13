#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const charList = JSON.parse(body).characters;
    printCharacters(charList, 0);
  }
});

function printCharacters (charList, i) {
  if (i >= charList.length) { return; }
  request.get(charList[i], function (error, response, body) {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      console.log(JSON.parse(body).name);
    }
    return printCharacters(charList, i + 1);
  });
}
