import React, { useState } from 'react';
import {
  Col, 
  Container, 
  Row,
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem
} from 'reactstrap';
import { Link } from 'react-router-dom';
import jwtDecode from 'jwt-decode';
import { CgProfile } from 'react-icons/cg';

import Navbar from './Navbar';
import './Header.css';

export default function Header() {
  const token = localStorage.getItem('token');

  const [ isProfileDropdownOpen, setIsProfileDropdownOpen ] = useState(false);

  const isTokenExpired = (token) => {
    if (!token) return true;
    const decodedToken = jwtDecode(token);
    const currentDate = new Date();
    return (decodedToken.exp * 1000) < currentDate.getTime();
  }

  const toggleProfileDropdown = () => {
    setIsProfileDropdownOpen(!isProfileDropdownOpen);
  }

  return (
    <Container fluid>
      <Row className='p-2 align-items-center'>
        <Col className='text-left'>
          <h1>StatComplete</h1>
        </Col>
        <Col className='text-end'>
          { isTokenExpired(token) ? 
              <Link className='btn btn-secondary' to='/login'>Sign In</Link> : 
              <Dropdown isOpen={isProfileDropdownOpen} toggle={toggleProfileDropdown}>
                <DropdownToggle className='p-0 m-0 profile-button'>
                  <CgProfile className='profile-icon' />
                </DropdownToggle>
                <DropdownMenu>
                  <DropdownItem><Link to='/'>Profile</Link></DropdownItem>
                  <DropdownItem><Link to='/'>Logout</Link></DropdownItem>
                </DropdownMenu>
              </Dropdown>
          }
        </Col>
      </Row>
      <Row>
        <Navbar />
      </Row>
    </Container>
  );
}