import { Cookies } from 'react-cookie';

import { privateAxios, publicAxios } from './axios';

const REGISTER_URL = 'register/';
const LOGIN_URL = 'login/';
const LOGOUT_URL = 'logout/';
const REFRESH_TOKEN_URL = 'login/refresh/';

const cookies = new Cookies();

const register = async (userRegistrationData) => {
  return await publicAxios.post(REGISTER_URL, userRegistrationData)
  .then(
    (response) => {
      if (response.data.refresh) {
        cookies.set('refresh', response.data.refresh, {
          httpOnly: true
        })
      }
      return response;
    }
  );
};

const login = async (username, password) => {
  return await publicAxios.post(LOGIN_URL, {
    username: username,
    password: password,
  })
  .then(
    (response) => {
      if (response.data.refresh) {
        cookies.set('refresh', response.data.refresh, {
          httpOnly: true
        })
      }
      return response;
    }
  );
};

const logout = async () => {
  privateAxios.post(LOGOUT_URL);
};

const refreshToken = async () => {
  privateAxios.post(REFRESH_TOKEN_URL);
}

const AuthApi = {
  register,
  login,
  logout,
  refreshToken,
};

export default AuthApi;