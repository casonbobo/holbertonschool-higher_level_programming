#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

function printFileContents (filePath) {
  fs.writeFile(filePath, content, 'utf-8', (err, content) => {
    if (err) {
      console.error(err);
    }
  });
}
