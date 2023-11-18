export default async function handleResponseFromAPI(promise) {
  const newPromise = promise
    .then((result) => { console.log('Got a response from the API'); return result; })
    .catch(() => new Error());

  await newPromise;

  return newPromise;
}
