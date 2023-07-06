import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import AccountCircle from '@mui/icons-material/AccountCircle';

import './index.css';
import { logout } from 'src/state/token/actions';
import PersonalInfo from './personalInfo';
import ContactInfo from './contactInfo';
import Loading from 'src/common/loading';
import Error from 'src/common/error';
import UserApi from 'src/api/user';

export default function UserProfile() {
  const navigate = useNavigate();

  const errorRef = useRef();
  
  const [ user, setUser ] = useState({});
  const [ loading, setLoading ] = useState(true);
  const [ errorMessage, setErrorMessage ] = useState('');

  const dispatch = useDispatch();

  useEffect(() => {
    UserApi.currentUser()
    .then(
      (response) => {
        setUser(response?.data);
        setLoading(false);
      },
      (error) => {
        setErrorMessage(error.message);
        setLoading(false);
      }
    );
  }, []);

  const logoutUser = () => {
    dispatch(logout());
    navigate('/');
  }

  return (
    <Box sx={{ flexGrow: 1 }} className='m-2'>
      <Grid container>
        <Grid item xs={6}>
          <Button
            variant='contained'
            disableElevation
            onClick={() => navigate(-1)}
          >
            Back
          </Button>
        </Grid>
        <Grid item xs={6} className='text-end'>
          <Button
            variant='contained'
            disableElevation
            onClick={logoutUser}
          >
            Log Out
          </Button>
        </Grid>
      </Grid>
      { loading ? 
          <Loading />
        :
          <>
            <Grid container>
              <Grid item xs={12}>
                <Error errorRef={errorRef} message={errorMessage} />
              </Grid>
            </Grid>
            { !errorMessage &&
              <>
                <Grid container>
                  <Grid item xs={12} className='m-2 text-center'>
                    <IconButton color='primary' className='p-0 m-0 user-logo'>
                      <AccountCircle sx={{ fontSize: '1250%' }}/>
                    </IconButton>
                  </Grid>
                </Grid>
                <Grid container>
                  <Grid item xs={12} className='m-2'>
                    <PersonalInfo user={user} />
                  </Grid>
                </Grid>
                <Grid container>
                  <Grid item xs={12} className='m-2'>
                    <ContactInfo user={user} />
                  </Grid>
                </Grid>
              </>
            }
          </>
      }
    </Box>
  );
}