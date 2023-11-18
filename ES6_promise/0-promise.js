export default function getResponseFromAPI() {
  function setPromise(resolve) {
    resolve();
  }
  return new Promise(setPromise);
}
