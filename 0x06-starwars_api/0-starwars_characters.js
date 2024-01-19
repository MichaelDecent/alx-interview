#!/usr/bin/node

const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/';

request(`${baseUrl}films/${process.argv[2]}/`, (error, response, body) => {
  if (error) {
    console.error('Request error:', error);
    return;
  }

  if (response.statusCode >= 200 && response.statusCode < 300) {
    const data = JSON.parse(body);

    data.characters.forEach((element) => {
      request(element, (error, response, body) => {
        if (error) {
          console.error('Request error:', error);
          return;
        }
        if (response.statusCode >= 200 && response.statusCode < 300) {
          const data = JSON.parse(body);
          console.log(data.name);
        } else {
          console.error(`HTTP error! Status: ${response.statusCode}`);
        }
      });
    });
  } else {
    console.error(`HTTP error! Status: ${response.statusCode}`);
  }
});
