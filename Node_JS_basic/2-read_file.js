const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot lead the database');
  }
  const dates = content.split('\n').slice(1);
  console.log(`Number of students: ${dates.length}`);

  const students = dates.map((student) => student.split(','));

  const studentsCsNames = students
    .filter((student) => student[3] === 'CS')
    .map((student) => student[0]);
  console.log(`Number of students in CS: ${studentsCsNames.length}: ${studentsCsNames.join(', ')}`);

  const studentsSweNames = students
    .filter((student) => student[3] === 'SWE')
    .map((student) => student[0]);
  console.log(`Number of students in SWE: ${studentsSweNames.length}: ${studentsSweNames.join(', ')}`);
}

module.exports = countStudents;
