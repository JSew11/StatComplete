import { useEffect, useState } from 'react';

import OrganizationApi from 'src/api/organization';

const OrganizationDetailsForm = ({ organizationId }) => {
  const [ organizationData, setOrganizationData ] = useState({});

  useEffect(() => {
    if (organizationId && organizationId !== '') {
      OrganizationApi.retrieve(organizationId)
      .then((response) => {
        setOrganizationData(response.data);
      });
    }
  }, []);

  return (
    <h3>TODO: Organization Details Form</h3>
  );
}

export default OrganizationDetailsForm;