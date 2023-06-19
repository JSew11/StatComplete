import { useEffect, useState } from 'react';

import Loading from 'src/components/loading';
import OrganizationApi from 'src/api/organization';

const OrganizationDetailsForm = ({ organizationId }) => {
  const [ loading, setLoading ] = useState(true);
  const [ organizationData, setOrganizationData ] = useState({});

  useEffect(() => {
    if (organizationId && organizationId !== '') {
      OrganizationApi.retrieve(organizationId)
      .then((response) => {
        setOrganizationData(response.data);
        setLoading(false);
        return response;
      });
    }
  }, []);

  return (
    <>
      { loading ? 
          <Loading />
        :
          <h3>TODO: Organization Details Form</h3>
      }
    </>
  );
}

export default OrganizationDetailsForm;