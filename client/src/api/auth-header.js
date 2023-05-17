export default function authHeader() {
  const accessToken = localStorage.getItem('token');

  if (accessToken) {
    return { Authorization: 'Bearer ' + accessToken };
  }
  return {};
}