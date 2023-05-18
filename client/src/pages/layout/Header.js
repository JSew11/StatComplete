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
import { useDispatch, useSelector} from 'react-redux';

import { logout } from '../../state/token/actions';

import Navbar from './Navbar';
import './Header.css';

export default function Header() {
  const navigate = useNavigate();

  const [ isProfileDropdownOpen, setIsProfileDropdownOpen ] = useState(false);

  const { isLoggedIn, access, refresh } = useSelector(state => state.auth);
  console.log(access);
  console.log(refresh);
  const dispatch = useDispatch();

  const toggleProfileDropdown = () => {
    setIsProfileDropdownOpen(!isProfileDropdownOpen);
  }

  const logoutUser = () => {
    dispatch(logout());
  }

  return (
    <Container fluid>
      <Row className='p-2 align-items-center'>
        <Col className='text-left'>
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
                <DropdownItem className='p-0'><NavLink className='user-dropdown-link' href='/'>Profile</NavLink></DropdownItem>
                <DropdownItem className='p-0'><NavLink className='user-dropdown-link' onClick={logoutUser} href='/'>Logout</NavLink></DropdownItem>
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