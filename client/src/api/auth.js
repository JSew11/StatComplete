import instance from './api';

const REGISTER_URL = 'register/';
const LOGIN_URL = 'login/';
const LOGOUT_URL = 'logout/';

const register = async (username, firstName, lastName, email, password) => {
  return await instance.post(REGISTER_URL, {
    first_name: firstName,
    last_name: lastName,
    username: username,
    email: email,
    password: password,
  })
  .then((response) => {
    if (response.data.access) {
      localStorage.setItem('token', response.data.access);
    }

    return response.data;
  });
};

const login = async (username, password) => {
  return await instance.post(LOGIN_URL, {
    username: username,
    password: password,
  })
  .then((response) => {
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

export default {
  register,
  login,
  logout,
};