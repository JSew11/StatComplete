import { publicAxios, privateAxios } from './axios';
import { Cookies } from 'react-cookie';

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
  .then((response) => {
    if (response.data.refresh) {
      try {
        cookies.set('refresh', response.data.refresh, {
          httpOnly: true,
          secure: true,
        });
      } catch (error) {
        return error;
      }
    }
    if (response.data.access) {
      localStorage.setItem('token', response.data.access);
    }

    return response.data;
  });
};

const login = async (username, password) => {
  return await publicAxios.post(LOGIN_URL, {
    username: username,
    password: password,
  })
  .then((response) => {
    if (response.data.refresh) {
      try {
        cookies.set('refresh', response.data.refresh, {
          httpOnly: true,
          secure: true,
        });
      } catch (error) {
        return error;
      }
    }
    if (response.data.access) {
      localStorage.setItem('token',response.data.access);
    }

    return response.data;
  });
};

const logout = () => {
  // TODO: call the logout api endpoint
  localStorage.removeItem('token');
};

const refreshToken = () => {
  privateAxios.post(REFRESH_TOKEN_URL)
  .then((response) => {
    if (response.data.access) {
      localStorage.setItem('token', response.data.access);
    }

    return response.data;
  });
}

export default {
  register,
  login,
  logout,
  refreshToken,
};