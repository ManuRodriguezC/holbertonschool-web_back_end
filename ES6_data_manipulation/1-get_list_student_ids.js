export default function getListStudentIds(dates) {
  if (!Array.isArray(dates)) {
    return [];
  }
  return dates.map((date) => date.id);
}
