export default function concatArrays(array1, array2, string) {
  let text = array1.join('') + array2.join('') + string;
  return text.split('')
}
