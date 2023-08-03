#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

function printFileContents (filePath) {
  fs.writeFile(filePath, 'utf8', (err) => {
    if (err) {
      console.error('Error:', err);
    } else {
      console.write(content);
    }
  });
}
printFileContents(filePath);
