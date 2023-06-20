import {
  Col, 
  Container, 
  Row,
} from 'reactstrap';
import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';

import Navbar from 'src/components/layout/navbar';
import UserDropdown from 'src/components/userDropdown';
import './index.css';

export default function Header() {
  const navigate = useNavigate();

  const { isLoggedIn } = useSelector(state => state.auth);
  
  return (
    <Container fluid>
      <Row className='p-2 align-items-center'>
        <Col onClick={() => {navigate('/');}} className='site-logo text-start'><h1>StatComplete</h1></Col>
        <Col className='m-0 p-0 text-end'><UserDropdown isLoggedIn={isLoggedIn} /></Col>
      </Row>
      <Row>
        <Navbar />
      </Row>
    </Container>
  );
}