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
      <Row className='m-2'>
        <Card>
          <CardHeader>Organization Details</CardHeader>
          <CardBody><OrganizationDetailsForm organizationId={organizationId}/></CardBody>
        </Card>
      </Row>
      <Row className='m-2'>
        <Card>
          <CardHeader>Baseball Competitions</CardHeader>
          <CardBody><BaseballCompetitionsTable organizationId={organizationId}/></CardBody>
        </Card>
      </Row>
    </Container>
  );
}

export default OrganizationHome;