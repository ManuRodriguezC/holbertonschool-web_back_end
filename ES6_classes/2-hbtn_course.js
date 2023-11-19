export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }


  get name() {
    return this.name;
  }
  
  set name(newName) {
    if (typeof(newName) !== 'string') {
      throw TypeError('Name must be a string');
    }
    this.name = newName;
  }

  get length () {
    return this.length;
  }

  set length(newlength) {
    if (typeof(newlength) !== 'number') {
      throw TypeError('Length must be a number');
    }
    this.length = newlength;
  }

  get students() {
    return this.students;
  }

  set students(newStudents) {
    if (typeof(newStudents) !== 'object') {
      throw TypeError('Students must be a array of Strings');
    }
    this.students = newStudents;
  }
}