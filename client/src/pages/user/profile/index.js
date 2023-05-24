import {
  Button,
  Container,
  Row,
  Col,
} from 'reactstrap';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { CgProfile } from 'react-icons/cg';

import './index.css';
import { logout } from 'src/state/token/actions';
import PersonalInfo from './PersonalInfo';
import ContactInfo from './ContactInfo';

export default function UserProfile() {
  const navigate = useNavigate();

  const dispatch = useDispatch();

  const logoutUser = () => {
    dispatch(logout());
    navigate('/');
  }

  return (
    <Container fluid>
      <Row className='p-2 align-items-center'>
        <Col className='text-start'><Button color='primary' onClick={() => {navigate(-1);}}>Back</Button></Col>
        <Col className='text-end'><Button color='primary' onClick={logoutUser}>Log Out</Button></Col>
      </Row>
      <Row className=' p-2 align-items-center'>
        <Col className='text-center'><CgProfile className='profile-logo'/></Col>
      </Row>
      <Row className='p-2 align-items-center'>
        {/* <Col className='text-center'><Button>Edit Profile Logo</Button></Col> */}
      </Row>
      <Row className='p-2'>
        <Col><PersonalInfo /></Col>
      </Row>
      <Row className='p-2'>
        <Col><ContactInfo /></Col>
      </Row>
      <Row className='p-2 align-items-center'>
        <Col className='text-end'><Button>Change Password</Button></Col>
        <Col className='text-start'><Button color='danger'>Delete Profile</Button></Col>
      </Row>
    </Container>
  );
}