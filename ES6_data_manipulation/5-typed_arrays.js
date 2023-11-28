export default function createInt8TypedArray(length, position, value) {
  const buffer = new DataView(new ArrayBuffer(length));
  try {
    buffer.setInt8(position, value);
  } catch (error) {
    throw new Error('Position outside range');
  }
  return buffer;
}
