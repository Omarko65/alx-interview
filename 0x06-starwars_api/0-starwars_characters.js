#!/usr/bin/node
/**
 * Script for printing out all Star Wars Characters
 */

const request = require('request');
const id = process.argv[2];
if (!id || isNaN(id)) {
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const responses = [];

  const json = JSON.parse(body);
  const characters = json.characters;

  characters.forEach((character) => {
    const url = character;
    const promise = new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        }
        resolve(JSON.parse(body).name);
      });
    });
    responses.push(promise);
  });
  Promise.all(responses)
    .then(names => console.log(names.join('\n')))
    .catch(errors => console.log(errors));
});
