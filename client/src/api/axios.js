import axios from 'axios';

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
});

export { publicAxios, privateAxios };