export default function getResponseFromAPI() {
  function setPromise(resolve, reject) {
    resolve();
  }
  return new Promise(setPromise);
}
