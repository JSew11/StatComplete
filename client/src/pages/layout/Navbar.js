import React, { Component } from 'react';
import {
  Container,
  Nav,
  NavItem,
  NavLink,
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem
} from 'reactstrap';
import './Navbar.css';

export default class Navbar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      'dropdownOpen': false,
    }
  }

  toggleDropdown = () => {
    this.setState({
      'dropdownOpen': !this.state.dropdownOpen
    });
  }

  render() {
    return (
      <Container fluid className='navbar p-0'>
        <Nav className='px-2'>
          <Dropdown nav 
            isOpen={this.state.dropdownOpen} 
            toggle={this.toggleDropdown}
          >
            <DropdownToggle nav caret className='link'>
              Sports
            </DropdownToggle>
            <DropdownMenu>
              <DropdownItem className='p-0'>
                <NavLink href='#' className='dropdown-link'>Baseball</NavLink>
              </DropdownItem>
            </DropdownMenu>
          </Dropdown>
          {/* TODO: show these links based on user permissions */}
          <NavItem>
            <NavLink href='#' className='link'>Organization</NavLink>
          </NavItem>
        </Nav>
      </Container>
    );
  }
}