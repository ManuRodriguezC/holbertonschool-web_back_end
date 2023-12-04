const express = require('express');
const fs = require('fs');

const database = process.argv[2];

function students(data) {
  const dates = data.split('\n').slice(1);
  const result = [`Number of students: ${dates.length}`];

  const students = dates.map((student) => student.split(','));

  const studentsCsNames = students
    .filter((student) => student[3] === 'CS')
    .map((student) => student[0]);
  result.push(`Number of students in CS: ${studentsCsNames.length}. List: ${studentsCsNames.join(', ')}`);

  const studentsSweNames = students
    .filter((student) => student[3] === 'SWE')
    .map((student) => student[0]);
  result.push(`Number of students in SWE: ${studentsSweNames.length}. List: ${studentsSweNames.join(', ')}`);

  return result;
}

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  let data;
  const datesStudents = 'This is the list of our students\n';
  try {
    data = fs.readFileSync(database, 'utf8');
  } catch (error) {
    response.status(500);
    response.send(`${datesStudents}Cannot load the database`);
    return;
  }
  response.status(200);
  response.send(datesStudents + students(data).join('\n'));
});

app.listen(port);

module.exports = app;
