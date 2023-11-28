export default function createInt8TypedArray(length, position, value) {
  const array =  new ArrayBuffer(length);
  const typeArray = new Int8Array(array)
  typeArray[position] = value;
  return typeArray;
}
