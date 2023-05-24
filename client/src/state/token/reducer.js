import {
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
  REFRESH_TOKEN,
} from 'src/state/actionTypes';

const token = sessionStorage.getItem('token');

const initialState = token ? {isLoggedIn: true, access: token} : { isLoggedIn: false, access: null};

export default function auth(state=initialState, action) {
  const { type, payload } = action;

  switch (type) {
    case REGISTER_SUCCESS:
      return {
        ...state,
        isLoggedIn: true,
        access: payload.access,
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
    case REFRESH_TOKEN: 
      return {
        ...state,
        isLoggedIn: true,
        access: payload.access,
      }
    default:
      return state;
  }
}