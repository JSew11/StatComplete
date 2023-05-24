import { applyMiddleware } from 'redux';
import { configureStore } from '@reduxjs/toolkit';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';

import auth from 'src/state/token/reducer';
import message from 'src/state/message/reducer';

const middleware = [thunk];

const store = configureStore(
  {
    reducer: {
      auth,
      message,
    }
  },
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;