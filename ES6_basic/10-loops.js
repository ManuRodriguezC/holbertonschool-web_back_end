export default function appendToEachArrayValue(array, appendString) {
  const list = [];
  for (const date of array) {
    list.push(appendString + date);
  }

  return list;
}
