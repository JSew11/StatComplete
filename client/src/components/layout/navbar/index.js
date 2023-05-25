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

export default function Navbar() {
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
        {/* TODO: show these links based on user permissions */}
        <NavItem>
          <NavLink className='link' href='/organization/'>Organization</NavLink>
        </NavItem>
      </Nav>
    </Container>
  );
}