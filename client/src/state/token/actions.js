import {
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
  SET_MESSAGE,
  REFRESH_TOKEN,
} from 'src/state/actionTypes';
import AuthApi from 'src/api/auth';

export const register = (userRegistrationData) => (dispatch) => {
  return AuthApi.register(userRegistrationData).then(
    (data) => {
      dispatch({
        type: REGISTER_SUCCESS,
        payload: data.access,
      });

      dispatch({
        type: SET_MESSAGE,
        payload: data.message,
      });

      return Promise.resolve();
    },
    (error) => {
      const message = 
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      dispatch({
        type: REGISTER_FAIL,
      });

      dispatch({
        type: SET_MESSAGE,
        payload: message,
      });

      return Promise.reject();
    }
  );
};

export const login = (username, password) => (dispatch) => {
  return AuthApi.login(username, password).then(
    (data) => {
      dispatch({
        type: LOGIN_SUCCESS,
        payload: data.access,
      });

      return Promise.resolve();
    },
    (error) => {
      let message = 'Login Failed';
      if (error.response && error.response.status === 401) {
        message = 'Invalid Login Credentials';
      } else {
        message =
          (error.response &&
            error.response.data &&
            error.response.data.message) ||
          error.message ||
          error.toString();
      }

      dispatch({
        type: LOGIN_FAIL,
      });

      dispatch({
        type: SET_MESSAGE,
        payload: message,
      });

      return Promise.reject();
    }
  );
}

export const logout = () => (dispatch) => {
  AuthApi.logout().then(
    () => {  
      dispatch({
        type: LOGOUT,
      });

      return Promise.resolve();
    },
    () => {
      return Promise.reject();
    }
  );
};

export const refreshToken = (access) => (dispatch) => {
  dispatch({
    type: REFRESH_TOKEN,
    payload: access,
  });
}