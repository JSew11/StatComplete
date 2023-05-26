import {
  SET_MESSAGE,
  CLEAR_MESSAGE
} from 'src/state/actionTypes';

export const setMessage = (message) => ({
  type: SET_MESSAGE,
  payload: {
    message: message
  },
});

export const clearMessage = () => ({
  type: CLEAR_MESSAGE,
});