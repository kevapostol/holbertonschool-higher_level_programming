#!/usr/bin/node
const request = require('request');
const uri = 'https://swapi-api.hbtn.io/api/films/';
request.get(uri, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const obj = JSON.parse(body);
    const results = obj.results;
    let count = 0;

    for (const eaFilm of results) {
      for (const eaCharacter of eaFilm.characters) {
        if (eaCharacter.indexOf('18') > -1) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
