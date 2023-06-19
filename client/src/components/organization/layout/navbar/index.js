import { useState } from 'react';
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

import './index.css';

export default function OrganizationNavbar() {
  const [ dropdownOpen, setDropdownOpen ] = useState(false);

  return (
    <Container fluid className='navbar p-0'>
      <Nav className='px-2'>
        <Dropdown nav 
          isOpen={dropdownOpen} 
          toggle={() => {setDropdownOpen(!dropdownOpen)}}
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
        <NavItem>
          <NavLink className='link' href='#'>Competitions</NavLink>
        </NavItem>
        <NavItem>
          <NavLink className='link' href='#'>Teams</NavLink>
        </NavItem>
      </Nav>
    </Container>
  );
}