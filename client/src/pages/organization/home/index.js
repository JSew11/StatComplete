import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import {
  Container,
  Row,
  Col,
  Card,
  CardHeader,
  CardBody,
} from 'reactstrap';

import OrganizationApi from 'src/api/organization';
import BaseballCompetitionsTable from 'src/components/baseball/competitionsTable';

const OrganizationHome = () => {
  const { organizationId } = useParams();

  const [ organizationData, setOrganizationData ] = useState({});

  useEffect(() => {
    OrganizationApi.retrieve(organizationId)
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
        <Col>
          <Card>
            <CardHeader>Baseball Competitions</CardHeader>
            <CardBody><BaseballCompetitionsTable organizationId={organizationId}/></CardBody>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default OrganizationHome;