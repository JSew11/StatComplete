import { publicAxios } from './axios';

import store from '../state/store';

const REGISTER_URL = 'register/';
const LOGIN_URL = 'login/';
const LOGOUT_URL = 'logout/';
const REFRESH_TOKEN_URL = 'login/refresh/';

const register = async (username, firstName, lastName, email, password) => {
  return await publicAxios.post(REGISTER_URL, {
    first_name: firstName,
    last_name: lastName,
    username: username,
    email: email,
    password: password,
  });
};

const login = async (username, password) => {
  return await publicAxios.post(LOGIN_URL, {
    username: username,
    password: password,
  });
};

const logout = async () => {
  const state = store.getState();

  publicAxios.post(LOGOUT_URL, {
    refresh: state.auth.refresh,
  });
};

const refreshToken = async () => {
  const state = store.getState();

  publicAxios.post(REFRESH_TOKEN_URL, {
    refresh: state.auth.refresh,
  });
}

const AuthApi = {
  register,
  login,
  logout,
  refreshToken,
};

export default AuthApi;