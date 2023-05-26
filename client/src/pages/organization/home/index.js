import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import {
  Container,
  Row,
  Col,
} from 'reactstrap';

import OrganizationApi from 'src/api/organization';

const OrganizationHome = () => {
  const {organizationId} = useParams();

  const [ organizationData, setOrganizationData ] = useState({});

  useEffect(() => {
    OrganizationApi.retrieveOrganization(organizationId)
    .then(
      (response) => {
        if (response.data) {
          setOrganizationData(response.data);
        }

        return response;
      }
    );
  }, [organizationId]);

  return (
    <Container fluid>
      <Row className='m-2'>
        <Col className='text-center'><h2>Organization Home</h2></Col>
      </Row>
    </Container>
  );
}

export default OrganizationHome;