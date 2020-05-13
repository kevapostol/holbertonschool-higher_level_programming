#!/usr/bin/node
const request = require('request');
const uri = 'https://swapi-api.hbtn.io/api/films/';
let count = 0;
request.get(uri, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body).results;
    for (const film of data) {
      for (const role of film.characters) {
        if (role.includes('18') === true) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
