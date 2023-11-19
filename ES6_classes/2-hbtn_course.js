class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new Error('name debe ser un string');
    }
    if (typeof length !== 'number') {
      throw new Error('length debe ser un número');
    }
    if (!Array.isArray(students)) {
      throw new Error('students debe ser un array');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }
 
  get name() {
    return this._name;
  }
 
  set name(value) {
    if (typeof value !== 'string') {
      throw new Error('name debe ser un string');
    }
    this._name = value;
  }
 
  get length() {
    return this._length;
  }
 
  set length(value) {
    if (typeof value !== 'number') {
      throw new Error('length debe ser un número');
    }
    this._length = value;
  }
 
  get students() {
    return this._students;
  }
 
  set students(value) {
    if (!Array.isArray(value)) {
      throw new Error('students debe ser un array');
    }
    this._students = value;
  }
 }