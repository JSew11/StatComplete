import { useState, useEffect } from 'react';
import {
  NavLink,
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem
} from 'reactstrap';
import { CgProfile } from 'react-icons/cg';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import './index.css';
import { logout } from 'src/state/token/actions';
import UserApi from 'src/api/user';

const UserDropdown = ({ isLoggedIn }) => {
  const navigate = useNavigate();

  const [ isProfileDropdownOpen, setIsProfileDropdownOpen ] = useState(false);
  const [ organizationHomeUrl, setOrganizationHomeUrl ] = useState('');

  const dispatch = useDispatch();

  useEffect(() => {
    if (isLoggedIn) {
      UserApi.currentUser()
      .then(
        (response) => {
          if (response.data.organization) {
            setOrganizationHomeUrl(`/organizations/${response.data.organization}/`);
          }
          return response;
        },
        (error) => {
          setOrganizationHomeUrl('');
          return error;
        }
      );
    }
  }, []);

  const toggleProfileDropdown = () => {
    setIsProfileDropdownOpen(!isProfileDropdownOpen);
  };

  const logoutUser = () => {
    dispatch(logout());
    navigate('/');
  };

  return (
    <>
      { isLoggedIn ?
        <Dropdown isOpen={isProfileDropdownOpen} toggle={toggleProfileDropdown}>
          <DropdownToggle className='p-0 m-0 profile-button'>
            <CgProfile className='profile-icon' />
          </DropdownToggle>
          <DropdownMenu>
            <DropdownItem className='py-0 text-end'><NavLink href='/profile/' className='user-dropdown-item'>My Profile</NavLink></DropdownItem>
            { organizationHomeUrl !== '' && <DropdownItem className='py-0 text-end'><NavLink href={organizationHomeUrl} className='user-dropdown-item'>Organization Home</NavLink></DropdownItem>}
            <DropdownItem className='py-0 text-end' onClick={logoutUser}>Log Out</DropdownItem>
          </DropdownMenu>
        </Dropdown>
        :
        <Link className='btn btn-primary' to='/login'>Sign In</Link> 
      }
    </>
  );
}

export default UserDropdown;