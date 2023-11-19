export default class ClassRoom {
  constructor(maxStudentsSize) {
   if (typeof maxStudentsSize !== 'number') {
     console.log('El valor debe ser un número');
     this._maxStudentsSize = 0;
   } else {
     this._maxStudentsSize = maxStudentsSize;
   }
  }
 
  get maxStudentsSize() {
   return this._maxStudentsSize;
  }
}
 