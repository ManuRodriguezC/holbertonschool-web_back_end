export default function handleResponseFromAPI(promise) {
  promise
    .then((result) => {
      console.log('Got a response from the API');
      return result;
    })
    .catch(() => new Error());
  return promise;
}