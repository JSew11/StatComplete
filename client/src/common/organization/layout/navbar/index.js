import { useState } from 'react';
import Menu from '@mui/material/Menu';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import KeyboardArrowDown from '@mui/icons-material/KeyboardArrowDown';

import './index.css';

export default function OrganizationNavbar({ organizationId }) {
  const [ anchorEl, setAnchorEl ] = useState(null);
  const isDropdownOpen = Boolean(anchorEl);

  const openSportsDropdown = (event) => {
    setAnchorEl(event.currentTarget);
  }

  const closeSportsDropDown = () => {
    setAnchorEl(null);
  }

  return (
    <AppBar position='static' color='primary' className='mx-0 px-1' elevation={0}>
      <Toolbar variant='dense' className='mx-0 px-0'>
        <Button id='sports-dropdown' aria-controls={isDropdownOpen ? 'sports-menu' : undefined}
            aria-haspopup='true' aria-expanded={isDropdownOpen ? 'true' : undefined}
            color='primary' variant='contained' disableElevation
            endIcon={<KeyboardArrowDown />} className='mx-0' onClick={openSportsDropdown}
            >
          Sports
        </Button>
        <Menu
          id='sports-menu'
          anchorEl={anchorEl}
          open={isDropdownOpen}
          onClose={closeSportsDropDown}
          MenuListProps={{
            'aria-labelledby': 'sports-dropdown',
          }}
        >
          <MenuItem href='#' onClick={closeSportsDropDown}>Baseball</MenuItem>
        </Menu>
        <Button color='primary' variant='contained' disableElevation
            href='#' className='mx-0 navbar-link'>
          Competitions
        </Button>
        <Button color='primary' variant='contained' disableElevation
            href='#' className='mx-0 navbar-link'>
          Teams
        </Button>
      </Toolbar>
    </AppBar>
  );
}