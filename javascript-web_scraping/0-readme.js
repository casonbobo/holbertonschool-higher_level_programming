#!usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

function printFileContents(filePath) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error("Error reading the file:", err);
    } else {
      console.log(data);
    }
  });
}
printFileContents(filePath);
