import { privateAxios } from 'src/api/axios';

export const ORGANIZATION_URL = 'organizations/';

const retrieve = async (organizationId) => {
  return await privateAxios.get(ORGANIZATION_URL + organizationId + '/');
};

const list_baseball_competitions = async (organizationId) => {
  const url = ORGANIZATION_URL + organizationId + '/baseball/competitions/';
  return await privateAxios.get(url);
}

const list_baseball_teams = async (organizationId) => {
  const url = ORGANIZATION_URL + organizationId + '/baseball/teams/';
  return await privateAxios.get(url);
}

const OrganizationApi = {
  retrieve,
  list_baseball_competitions,
  list_baseball_teams,
};

export default OrganizationApi;