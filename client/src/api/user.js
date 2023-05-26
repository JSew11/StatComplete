import { privateAxios } from './axios';

const USER_URL = 'users/';

const currentUser = async () => {
  return await privateAxios.get(USER_URL + 'me/');
}

const retrieveUser = async (user_id) => {
  return await privateAxios.get(USER_URL + user_id + '/');
}

const partialUpdateUser = async (user_id, updated_fields) => {
  return await privateAxios.patch(USER_URL + user_id + '/', updated_fields);
}

const UserApi = {
  currentUser,
  retrieveUser,
  partialUpdateUser,
}

export default UserApi;