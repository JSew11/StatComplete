import { useParams } from 'react-router-dom';
import {
  Container,
  Row,
  Col,
  Card,
  CardHeader,
  CardBody,
} from 'reactstrap';

import BaseballCompetitionsTable from 'src/components/baseball/competitionsTable';
import OrganizationDetailsForm from '../../../components/organization/detailsForm';

const OrganizationHome = () => {
  const { organizationId } = useParams();

  return (
    <Container fluid>
      <Row className='p-2'>
        <Col>
          <Card>
            <CardHeader>Organization Details</CardHeader>
            <CardBody><OrganizationDetailsForm organizationId={organizationId}/></CardBody>
          </Card>
        </Col>
      </Row>
      <Row className='p-2'>
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