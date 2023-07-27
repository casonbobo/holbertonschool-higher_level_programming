#!/usr/bin/node
const argsText = process.argv.slice[2];

if (argsText[0]) {
  console.log(argsText);
} else {
  console.log('No argument');
}
