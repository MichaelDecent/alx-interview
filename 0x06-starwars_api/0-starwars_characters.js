#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

async function getRequest () {
  try {
    const result = await makeRequest(url);
    for (const element of result.characters) {
      try {
        const data = await makeRequest(element);
        console.log(data.name);
      } catch (error) {
        console.error('Request error:', error);
      }
    }
  } catch (error) {
    console.error('Request error:', error);
  }
}

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(new Error(`Request error: ${error}`));
        return;
      }

      if (response.statusCode >= 200 && response.statusCode < 300) {
        const data = JSON.parse(body);
        resolve(data);
      } else {
        reject(new Error(`HTTP error! Status: ${response.statusCode}`));
      }
    });
  });
}

getRequest();
