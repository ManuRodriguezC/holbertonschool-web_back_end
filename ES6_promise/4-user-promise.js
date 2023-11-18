export default function signUpUser(firstName, lastName) {
  const result = new Promise((resolve, reject) => {
    resolve({'firstName': firstName, 'lastName': lastName});
    reject({'Not found': firstName});
  });
  return result;
}