export default function cleanSet(set, startString) {
  if (!startString) return '';

  const filteredValues = Array.from(set).filter((value) => value.startsWith(startString));

  const mappedValues = filteredValues.map((value) => value.split(startString)[1]);

  return mappedValues.join('-').toString();
}
