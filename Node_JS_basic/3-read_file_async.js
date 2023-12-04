const fs = require('fs').promises;

function studentsTextOutput(data) {
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

module.exports = function countStudents(path) {
  return fs.readFile(path, { encoding: 'utf8' })
    .then((result) => {
      studentsTextOutput(result)
        .forEach((line) => console.log(line));
    })
    .catch(() => { throw new Error('Cannot load the database'); });
};
