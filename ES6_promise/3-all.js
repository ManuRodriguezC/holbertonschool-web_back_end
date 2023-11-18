import { createUser, uploadPhoto } from './utils.js';

export default function handleProfileSignup() {
  return Promise.all([createUser(), uploadPhoto()])
    .then(([user, photo]) => {
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    });
}
