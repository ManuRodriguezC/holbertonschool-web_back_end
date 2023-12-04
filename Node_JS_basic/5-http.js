const http = require('http');
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

const app = http.createServer((request, response) => {
  if (request.url === '/' || request.url === '') {
    response.writeHead(200);
    response.end('Hello Holberton School!');
  } else if (request.url === '/students' || request.url === '/students/') {
    let data;
    try {
      data = fs.readFileSync(database, 'utf8');
    } catch (error) {
      response.writeHead(500);
      response.end('Cannot load the database');
    }

    response.writeHead(200);
    let datesStudents = 'This is the list of our students\n';
    datesStudents += students(data).join('\n');
    response.end(datesStudents);
  } else {
    response.writeHead(404);
    response.end('Not found URL');
  }
});
app.listen(1245, 'localhost');

module.exports = app;
