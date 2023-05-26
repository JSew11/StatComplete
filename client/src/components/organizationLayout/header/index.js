import { useState, useEffect } from 'react';
import {
  Col, 
  Container, 
  Row,
} from 'reactstrap';
import { useParams, useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';

import UserDropdown from 'src/components/userDropdown';
import './index.css';
import OrganizationNavbar from '../navbar';
import OrganizationApi from 'src/api/organization';

export default function OrganizationHeader() {
  const {organizationId} = useParams();
  
  const navigate = useNavigate();

  const [ organizationName, setOrganizatioName ] = useState('');

  const { isLoggedIn } = useSelector(state => state.auth);

  useEffect(() => {
    OrganizationApi.retrieveOrganization(organizationId)
    .then(
      (response) => {
        if (response.data) {
          setOrganizatioName(response.data.name);
        }

        return response;
      }
    );
  }, [organizationId]);

  return (
    <Container fluid>
      <Row className='p-2 align-items-center'>
        <Col onClick={() => {navigate('/');}} className='small-logo col-1 text-start'><h2>SC</h2></Col>
        <Col className='text-center'><h1>{organizationName}</h1></Col>
        <Col className='col-1 text-end'><UserDropdown isLoggedIn={isLoggedIn} /></Col>
      </Row>
      <Row>
        <OrganizationNavbar />
      </Row>
    </Container>
  );
}