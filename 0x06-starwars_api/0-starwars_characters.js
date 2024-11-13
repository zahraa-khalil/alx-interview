#!/usr/bin/node

const https = require('https');
const args = process.argv;
const movieId = args[2];

const options = {
  hostname: 'swapi-api.alx-tools.com',
  port: 443,
  path: `/api/films/${movieId}/`,
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
};

function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    https.get(url, (resp) => {
      let data = '';

      resp.on('data', (chunk) => {
        data += chunk;
      });

      resp.on('end', () => {
        try {
          const characterData = JSON.parse(data);
          resolve(characterData.name);
        } catch (error) {
          Error(`Error parsing JSON from ${url}: ${error.message}`);
        }
      });
    }).on('error', (err) => {
      Error(`Request error for ${url}: ${err.message}`);
    });
  });
}

const req = https.request(options, (resp) => {
  let data = '';
  resp.on('data', (chunk) => {
    data += chunk;
  });

  resp.on('end', () => {
    try {
      const jsonData = JSON.parse(data);
      // console.log('Parsed JSON data:', jsonData.characters);
      const characters = jsonData.characters;

      Promise.all(characters.map(url => fetchCharacter(url)))
        .then(responses => {
          responses.forEach(character => {
            console.log(character);
          });
        })
        .catch(error => {
          console.error('An error occurred:', error);
        });
    } catch (error) {
      console.error('Error parsing JSON:', error.message);
    }
  });
});

// Enhanced error handling
req.on('error', (err) => {
  console.error('Request error:', err.message);
});

req.end();
