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

      if (response.data.access) {
        localStorage.setItem('token', response.data.access);
      }

      return response;
    }
  );
};

const login = async (email, password) => {
  return await publicAxios.post(LOGIN_URL, {
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

      if (response.data.access) {
        localStorage.setItem('token', response.data.access);
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