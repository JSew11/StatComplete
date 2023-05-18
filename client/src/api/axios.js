import axios from 'axios';

import { refreshToken } from '../state/token/actions';

const API_BASE_URL = process.env.REACT_APP_API_URL;

const publicAxios = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

const privateAxios = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

privateAxios.interceptors.request.use(
  async (config) => {
    const accessToken = localStorage.getItem('token');

    if (accessToken && accessToken != '') {
      config.headers = {
        ...config.headers,
        authorization: `Bearer ${accessToken}`,
      };
    }

    return config;
  },
  (error) => Promise.reject(error)
);

privateAxios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const config = error?.config;

    if (error?.response?.status === 401 && config?.sent) {
      config.sent = true;

      try {
        refreshToken();
        return privateAxios(config);
      } catch (refreshEerror) {
        return Promise.reject(refreshEerror);
      }
    }
    return Promise.reject(error);
  }
);

export { publicAxios, privateAxios };