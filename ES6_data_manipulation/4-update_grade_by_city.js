export default function updateStudentGradeByCity(students, city, newGrades) {
  const gradesMap = newGrades.reduce((acc, grade) => {
    acc[grade.studentId] = grade.grade;
    return acc;
  }, {});

  const updatedStudents = students
    .filter((student) => student.location === city)
    .map((student) => {
      const newGrade = gradesMap[student.id] || 'N/A';
      return { ...student, grade: newGrade };
    });
 
  return updatedStudents;
}
