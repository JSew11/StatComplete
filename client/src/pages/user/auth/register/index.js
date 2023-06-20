import { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useDispatch, useSelector } from 'react-redux';

import './index.css';
import { publicAxios } from 'src/api/axios';
import { register } from 'src/state/token/actions';
import { clearMessage } from 'src/state/message/actions';
import Error from 'src/components/error';

const CHECK_EMAIL_URL = 'check_email/'
const MINIMUM_PASSWORD_LENGTH = 7;
const REQUIRED_FIELD_MESSAGE = 'This field is required.';

export default function Register() {
  const navigate = useNavigate();

  const emailRef = useRef();
  const errorRef = useRef();

  const [ firstName, setFirstName ] = useState('');
  const [ firstNameErrorMsg, setFirstNameErrorMsg ] = useState(REQUIRED_FIELD_MESSAGE);
  const [ middleName, setMiddleName ] = useState('');
  const [ lastName, setLastName ] = useState('');
  const [ lastNameErrorMsg, setLastNameErrorMsg ] = useState(REQUIRED_FIELD_MESSAGE);
  const [ suffix, setSuffix ] = useState('');
  const [ email, setEmail ] = useState('');
  const [ emailErrorMsg, setEmailErrorMsg ] = useState(REQUIRED_FIELD_MESSAGE)
  const [ password, setPassword ] = useState('');
  const [ passwordErrorMsg, setPasswordErrorMsg ] = useState(REQUIRED_FIELD_MESSAGE)
  const [ confirmPassword, setConfirmPassword ] = useState('');
  const [ confirmPasswordErrorMsg, setConfirmPasswordErrorMsg ] = useState(REQUIRED_FIELD_MESSAGE)
  
  const { message } = useSelector(state => state.message);
  const dispatch = useDispatch();

  useEffect(() => {
    emailRef.current.focus();
  }, []);

  useEffect(() => {
    clearMessage();
  }, [firstName, middleName, lastName, suffix, email, password, confirmPassword])

  useEffect(() => {
    const checkEmail = async () => {
      try {
        const response = await publicAxios.post(
          CHECK_EMAIL_URL,
          JSON.stringify({
            email: email,
          })
        );
        if (response?.data?.email_available) {
          setEmailErrorMsg('');
        } else {
          setEmailErrorMsg('This email is not available.');
        }
      } catch (err) {
        setEmailErrorMsg('Could not determine if email is available. Please try again later.')
      }
    }

    const delayCheckEmail = setTimeout(() => {
      if (email !== '') {
        let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (re.test(email)) {
          checkEmail();
        } else {
          setEmailErrorMsg('Invalid email format.');
        }
      } else {
        setEmailErrorMsg(REQUIRED_FIELD_MESSAGE);
      }
    }, 1000);

    return () => {
      setEmailErrorMsg('Validating email.')
      clearTimeout(delayCheckEmail);
    };
  }, [email]);

  useEffect(() => {
    if (firstName !== '') {
      setFirstNameErrorMsg('');
    } else {
      setFirstNameErrorMsg(REQUIRED_FIELD_MESSAGE);
    }
  }, [firstName])

  useEffect(() => {
    if (lastName !== '') {
      setLastNameErrorMsg('');
    } else {
      setLastNameErrorMsg(REQUIRED_FIELD_MESSAGE);
    }
  }, [lastName])

  useEffect(() => {
    if (password !== '' || confirmPassword !== '') {
      if (password.length < MINIMUM_PASSWORD_LENGTH) {
        setPasswordErrorMsg(`Password must be at least ${MINIMUM_PASSWORD_LENGTH} characters long.`)
      } else if (password !== confirmPassword) {
        setPasswordErrorMsg('Passwords must match.')
      } else {
        setPasswordErrorMsg('');
      }
      if (password !== confirmPassword) {
        setConfirmPasswordErrorMsg('Passwords must match.')
      } else {
        setConfirmPasswordErrorMsg('');
      }
    } else {
      setPasswordErrorMsg(REQUIRED_FIELD_MESSAGE);
      setConfirmPasswordErrorMsg(REQUIRED_FIELD_MESSAGE);
    }
  }, [password, confirmPassword]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userRegistrationData = {
      first_name: firstName,
      last_name: lastName,
      email: email,
      password: password,
    }

    if (middleName !== '') {
      userRegistrationData['middle_name'] = middleName;
    }

    if (suffix !== '') {
      userRegistrationData['suffix'] = suffix;
    }

    dispatch(register(userRegistrationData))
      .then(() => {
        navigate('/');
      });
  }

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container>
        <Grid item xs={12}>
          <h2 className='p-1 m-1 text-center'>New StatComplete Account</h2>
        </Grid>
      </Grid>
      <Grid container>
        <Grid item xs={12}>
          <Error errorRef={errorRef} message={message}/>
        </Grid>
      </Grid>
      <Grid container className='justify-content-center'>
        <Grid item xs={8}>
          <Box
            component='form'
            autoComplete='off'
            sx={{ flexGrow: 1 }}
            className='m-2'
          >
            <Grid container className='p-2 justify-content-center'>
              <Grid item xs={12}>
                <TextField
                  required
                  type='text'
                  label='Email'
                  variant='outlined'
                  ref={emailRef}
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  fullWidth
                  error={emailErrorMsg !== ''}
                  helperText={emailErrorMsg}
                />
              </Grid>
            </Grid>
            <Grid container className='p-2 justify-content-center'>
              <Grid item xs={12}>
                <TextField
                  required
                  type='text'
                  label='First Name'
                  variant='outlined'
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  fullWidth
                  error={firstNameErrorMsg !== ''}
                  helperText={firstNameErrorMsg}
                />
              </Grid>
            </Grid>
            <Grid container className='p-2 justify-content-center'>
              <Grid item xs={12}>
                <TextField
                  type='text'
                  label='Middle Name'
                  variant='outlined'
                  value={middleName}
                  onChange={(e) => setMiddleName(e.target.value)}
                  fullWidth
                />
              </Grid>
            </Grid>
            <Grid container className='p-2 justify-content-center'>
              <Grid item xs={12}>
                <TextField
                  required
                  type='text'
                  label='Last Name'
                  variant='outlined'
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                  fullWidth
                  error={lastNameErrorMsg !== ''}
                  helperText={lastNameErrorMsg}
                />
              </Grid>
            </Grid>
            <Grid container className='p-2 justify-content-center'>
              <Grid item xs={12}>
                <TextField
                  type='text'
                  label='Suffix'
                  variant='outlined'
                  value={suffix}
                  onChange={(e) => setSuffix(e.target.value)}
                  fullWidth
                />
              </Grid>
            </Grid>
            <Grid container className='p-2 justify-content-center'>
              <Grid item xs={12}>
                <TextField
                  required
                  type='password'
                  label='Password'
                  variant='outlined'
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  fullWidth
                  error={passwordErrorMsg !== ''}
                  helperText={passwordErrorMsg}
                />
              </Grid>
            </Grid>
            <Grid container className='p-2 justify-content-center'>
              <Grid item xs={12}>
                <TextField
                  required
                  type='password'
                  label='Confirm Password'
                  variant='outlined'
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  fullWidth
                  error={confirmPasswordErrorMsg !== ''}
                  helperText={confirmPasswordErrorMsg}
                />
              </Grid>
            </Grid>
            <Grid container className='p-2'>
              <Grid item xs={6}>
                <Button 
                  type='submit' 
                  color='primary' 
                  variant='contained'
                  disableElevation
                  disabled={
                    emailErrorMsg !== '' ||
                    firstNameErrorMsg !== '' ||
                    lastNameErrorMsg !== '' ||
                    passwordErrorMsg !== '' ||
                    confirmPasswordErrorMsg !== ''
                  }
                  onClick={handleSubmit}
                >
                  Register
                </Button>
              </Grid>
              <Grid item xs={6} className='text-end'>
                <Button
                  color='error'
                  variant='contained'
                  disableElevation
                  href='/'
                  className='cancel-btn'
                >
                  Cancel
                </Button>
              </Grid>
            </Grid>
          </Box>
        </Grid>
      </Grid>
      <Grid container className='justify-content-center'>
        <Grid item xs={6}>
          <p className='text-center'>
            Already have an Account?
            <br/>
            <Button 
              color='primary'
              variant='contained'
              disableElevation
              href='/login'
              className='my-1 register-link-btn'
            >
              Sign In Here
            </Button>
          </p>
        </Grid>
      </Grid>
    </Box>
  );
}