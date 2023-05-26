import { privateAxios } from './axios';

const ORGANIZATION_URL = 'organizations/';

const retrieveOrganization = async (organizationId) => {
  return await privateAxios.get(ORGANIZATION_URL + organizationId + '/');
};

const OrganizationApi = {
  retrieveOrganization
};

export default OrganizationApi;