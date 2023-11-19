export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  
  get name() {
    return this._name;
  }
  
  set name(newName) {
    if (typeof(newName) !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = newName;
  }

  get length () {
    return this._length;
  }

  set length(newlength) {
    if (typeof(newlength) !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = newlength;
  }

  get students() {
    return this.students;
  }

  set students(newStudents) {
    if (typeof(newStudents) !== 'object') {
      throw TypeError('Students must be a array of Strings');
    }
    this._students = newStudents;
  }
}