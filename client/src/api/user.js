import { privateAxios } from './axios';

const USER_URL = 'users/';

const retrieve_user = async (user_id) => {
  return await privateAxios.get(USER_URL + user_id + '/');
}

const partial_update_user = async (user_id, updated_fields) => {
  return await privateAxios.patch(USER_URL + user_id + '/', updated_fields);
}

const UserApi = {
  retrieve_user,
  partial_update_user,
}

export default UserApi;