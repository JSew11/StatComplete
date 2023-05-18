import { Cookies } from 'react-cookie';

import { publicAxios } from './axios';

const REGISTER_URL = 'register/';
const LOGIN_URL = 'login/';
const LOGOUT_URL = 'logout/';
const REFRESH_TOKEN_URL = 'login/refresh/';

const cookies = new Cookies();

const register = async (username, firstName, lastName, email, password) => {
  return await publicAxios.post(REGISTER_URL, {
    first_name: firstName,
    last_name: lastName,
    username: username,
    email: email,
    password: password,
  })
  .then(
    (response) => {
      if (response.data.refresh) {
        cookies.set('refresh', response.data.refresh, {
          httpOnly: true
        })
      }
    }
  );
};

const login = async (username, password) => {
  return await publicAxios.post(LOGIN_URL, {
    username: username,
    password: password,
  });
};

const logout = async () => {
  publicAxios.post(LOGOUT_URL);
};

const refreshToken = async () => {
  publicAxios.post(REFRESH_TOKEN_URL);
}

const AuthApi = {
  register,
  login,
  logout,
  refreshToken,
};

export default AuthApi;