#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (parseInt(process.argv[2] < 1)) {

} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
