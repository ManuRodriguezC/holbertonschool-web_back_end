export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch(error) {
    queue.push(error.toString());
  }
  queue.push('Guardrail was processe');
  return queue;
}
