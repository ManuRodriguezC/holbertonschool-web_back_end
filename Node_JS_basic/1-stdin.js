const rl = require('readline');

rl.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  console.log(`Your name is: ${name}!`);
  if (name === 'Jhon') {
    console.log('This important software is now closing');
  }
  rl.close();
});
