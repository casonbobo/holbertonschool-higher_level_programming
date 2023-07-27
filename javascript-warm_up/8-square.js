#!/usr/bin/node
const side = process.argv[2];

for (let i = 0; i < side; i++) {
  for (let x = 0; x < side; x++) {
    process.stdout.write('X');
  }
  console.log('');
}
