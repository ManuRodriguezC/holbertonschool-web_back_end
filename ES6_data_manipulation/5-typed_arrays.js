export default function createInt8TypedArray(length, position, value) {
  const buffer = new DataView(new ArrayBuffer(length));
  buffer.setInt8(position,value);
  return buffer;
}
