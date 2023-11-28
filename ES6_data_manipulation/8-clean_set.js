export default function cleanSet(set, startString) {
  if (!startString) return '';

  let filteredValues = Array.from(set).filter(value => value.startsWith(startString));

  let mappedValues = filteredValues.map(value => value.split(startString)[1]);

  return mappedValues.join('-');
}
 