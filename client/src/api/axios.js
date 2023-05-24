import axios from 'axios';

import store from '../state/store';
import AuthApi from './auth';
import { refreshToken } from '../state/token/actions';

const API_BASE_URL = process.env.REACT_APP_API_URL;

const publicAxios = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

const privateAxios = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

privateAxios.interceptors.request.use(
  async (config) => {
    const state = store.getState();
    const accessToken = state.auth.access;

    if (accessToken && accessToken !== '') {
      config.headers = {
        ...config.headers,
        authorization: `Bearer ${accessToken}`,
      };
    }

    return config;
  },
  (error) => Promise.reject(error)
);

const { dispatch } = store;
privateAxios.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const config = error?.config;

    if (error?.response?.status === 401 && !config?._retry) {
      config._retry = true;

      try {
        const response = await AuthApi.refreshToken();
        dispatch(refreshToken(response.data.access));
        return privateAxios(config);
      } catch (refreshError) {
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  }
);

export { publicAxios, privateAxios };