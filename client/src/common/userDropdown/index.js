import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import AccountCircle from '@mui/icons-material/AccountCircle';

import './index.css';
import { logout } from 'src/state/token/actions';
import UserApi from 'src/api/user';

const UserDropdown = ({ isLoggedIn }) => {
  const navigate = useNavigate();

  const [ anchorEl, setAnchorEl ] = useState(null);
  const isDropdownOpen = Boolean(anchorEl);
  const [ organizationUrl, setOrganizationUrl ] = useState('');

  const dispatch = useDispatch();

  useEffect(() => {
    if (isLoggedIn) {
      UserApi.currentUser()
      .then(
        (response) => {
          if (response.data.organization) {
            setOrganizationUrl(`/organizations/${response.data.organization}/`);
          }
          return response;
        },
        (error) => {
          setOrganizationUrl('');
          return error;
        }
      );
    }
  }, []);

  const openUserDropdown = (event) => {
    setAnchorEl(event.currentTarget);
  }

  const closeUserDropdown = () => {
    setAnchorEl(null);
  }

  const logoutUser = () => {
    dispatch(logout());
    navigate('/');
  };

  return (
    <>
      { isLoggedIn ?
        <>
          <IconButton id='user-dropdown' aria-label='user-dropdown'
              aria-controls={isDropdownOpen ? 'user-menu' : undefined}
              aria-haspopup='true' aria-expanded={isDropdownOpen ? 'true' : undefined}
              size='large' color='primary' className='p-0 mx-3 user-icon'
              onClick={openUserDropdown}>
            <AccountCircle fontSize='inherit'/>
          </IconButton>
          <Menu
            id='user-menu'
            anchorEl={anchorEl}
            open={isDropdownOpen}
            onClose={closeUserDropdown}
            MenuListProps={{
              'aria-labelledby': 'user-dropdown',
            }}
          >
            <MenuItem onClick={() => navigate('/profile/')}>Profile</MenuItem>
            { organizationUrl !== '' && <MenuItem onClick={() => navigate(organizationUrl)}>Organization</MenuItem> }
            <MenuItem onClick={logoutUser}>Logout</MenuItem>
          </Menu>
        </>
        :
        <Button color='primary' variant='contained' disableElevation href='/login'
             className='sign-in-btn'>
          Sign In
        </Button> 
      }
    </>
  );
}

export default UserDropdown;