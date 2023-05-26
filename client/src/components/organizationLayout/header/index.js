import {
  Col, 
  Container, 
  Row,
} from 'reactstrap';
import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';

import UserDropdown from 'src/components/userDropdown';
import './index.css';
import OrganizationNavbar from '../navbar';

export default function OrganizationHeader() {
  const navigate = useNavigate();

  const { isLoggedIn } = useSelector(state => state.auth);

  return (
    <Container fluid>
      <Row className='p-2 align-items-center'>
        <Col onClick={() => {navigate('/');}} className='small-logo col-1 text-start'><h2>SC</h2></Col>
        <Col className='text-center'><h1>Organization Name</h1></Col>
        <Col className='col-1 text-end'><UserDropdown isLoggedIn={isLoggedIn} /></Col>
      </Row>
      <Row>
        <OrganizationNavbar />
      </Row>
    </Container>
  );
}