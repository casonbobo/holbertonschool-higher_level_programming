#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const website = 'https://swapi-api.hbtn.io/api/films/' + url;

request(website, function (err, response, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
