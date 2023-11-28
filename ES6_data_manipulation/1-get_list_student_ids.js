export default function getListStudentIds(dates) {
  if (!Array.isArray(dates)) {
    return []
  } else {
    return dates.map((date) => date.id)
  }
}
