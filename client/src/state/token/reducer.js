import {
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
  REFRESH_TOKEN_SUCCESS,
  REFRESH_TOKEN_FAIL,
} from '../actionTypes';

const accessToken = localStorage.getItem('token');

const initialState = accessToken ? {isLoggedIn: true, access: accessToken } : { isLoggedIn: false, access: null}

export default function (state=initialState, action) {
  const { type, payload } = action;

  switch (type) {
    case REGISTER_SUCCESS:
      return {
        ...state,
        isLoggedIn: false,
      };
    case REGISTER_FAIL:
      return {
        ...state,
        isLoggedIn: false,
      };
    case LOGIN_SUCCESS:
      return {
        ...state,
        isLoggedIn: true,
        access: payload.access,
      };
    case LOGIN_FAIL:
      return {
        ...state,
        isLoggedIn: false,
        access: null,
      };
    case LOGOUT:
      return {
        ...state,
        isLoggedIn: false,
        access: null,
      };
    case REFRESH_TOKEN_SUCCESS: 
      return {
        ...state,
        isLoggedIn: true,
        access: payload.access,
      }
    case REFRESH_TOKEN_FAIL:
      return {
        ...state,
        isLoggedIn: false,
        access: null,
      }
    default:
      return state;
  }
}