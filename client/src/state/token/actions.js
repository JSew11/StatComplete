import {
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
  REFRESH_TOKEN_SUCCESS,
  REFRESH_TOKEN_FAIL,
  SET_MESSAGE,
} from '../actionTypes';
import AuthApi from '../../api/auth';

export const register = (username, firstName, lastName, email, password) => (dispatch) => {
  return AuthApi.register(username, firstName, lastName, email, password).then(
    (data) => {
      dispatch({
        type: REGISTER_SUCCESS,
        payload: {
          refresh: data.refresh,
          access: data.access,
        }
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
        payload: {
          refresh: data.refresh,
          access: data.access,
        }
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
  AuthApi.logout();

  dispatch({
    type: LOGOUT,
  });
};

export const refreshToken = () => (dispatch) => {
  return AuthApi.refreshToken().then(
    (data) => {
      dispatch({
        type: REFRESH_TOKEN_SUCCESS,
        payload: {
          access: data.access,
        }
      });

      return Promise.resolve();
    },
    (error) => {
      let message = 'Token refresh failed.';
      if (error.response && error.response.status === 401) {
        message = 'Refresh token expired, please login again.';
      } else {
        message =
          (error.response &&
            error.response.data &&
            error.response.data.message) ||
          error.message ||
          error.toString();
      }

      dispatch({
        type: REFRESH_TOKEN_FAIL
      });

      dispatch({
        type: SET_MESSAGE,
        payload: message,
      });

      return Promise.reject();
    }
  );
}