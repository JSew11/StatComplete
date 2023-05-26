import {
  SET_MESSAGE,
  CLEAR_MESSAGE,
} from 'src/state/actionTypes';

const initialState = { message: '' };

export default function message(state=initialState, {type, payload}) {
  switch (type) {
    case SET_MESSAGE:
      return {
        message: payload.message
      };

    case CLEAR_MESSAGE:
      return {
        message: ''
      };

    default:
      return state;
  }
};