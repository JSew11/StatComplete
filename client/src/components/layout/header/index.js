import React, { useState } from 'react';
import {
  NavLink,
  Col, 
  Container, 
  Row,
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem
} from 'reactstrap';
import { Link, useNavigate } from 'react-router-dom';
import { CgProfile } from 'react-icons/cg';
import { useDispatch, useSelector } from 'react-redux';

import { logout } from 'src/state/token/actions';
import Navbar from 'src/components/layout/navbar';
import './index.css';

export default function Header() {
  const navigate = useNavigate();

  const [ isProfileDropdownOpen, setIsProfileDropdownOpen ] = useState(false);

  const { isLoggedIn } = useSelector(state => state.auth);
  const dispatch = useDispatch();

  const toggleProfileDropdown = () => {
    setIsProfileDropdownOpen(!isProfileDropdownOpen);
  }

  const logoutUser = () => {
    dispatch(logout());
    navigate('/');
  }

  return (
    <Container fluid>
      <Row className='p-2 align-items-center'>
        <Col onClick={() => {navigate('/');}} className='site-logo text-start'>
          <h1>StatComplete</h1>
        </Col>
        <Col className='text-end'>
          { isLoggedIn === false ?
            <Link className='btn btn-primary' to='/login'>Sign In</Link> 
            : 
            <Dropdown isOpen={isProfileDropdownOpen} toggle={toggleProfileDropdown}>
              <DropdownToggle className='p-0 m-0 profile-button'>
                <CgProfile className='profile-icon' />
              </DropdownToggle>
              <DropdownMenu>
                <DropdownItem className='p-0'><NavLink className='user-dropdown-link' href='/profile/'>Profile</NavLink></DropdownItem>
                <DropdownItem className='p-0' onClick={logoutUser}><NavLink className='user-dropdown-link' href='#'>Log Out</NavLink></DropdownItem>
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