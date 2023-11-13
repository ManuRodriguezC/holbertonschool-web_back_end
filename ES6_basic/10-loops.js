export default function appendToEachArrayValue(array, appendString) {
  let list = []
  for (var idx of array) {
    list.push(appendString + idx)
  }

  return list;
}
