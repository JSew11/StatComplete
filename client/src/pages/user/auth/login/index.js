import { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import FormControl from '@mui/material/FormControl';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputAdornment from '@mui/material/InputAdornment';
import InputLabel from '@mui/material/InputLabel';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';

import './index.css';
import { login } from 'src/state/token/actions';
import { clearMessage } from 'src/state/message/actions';
import Error from 'src/components/error';


export default function Login() {
  const navigate = useNavigate();

  const errorRef = useRef();
  const emailRef = useRef();

  const [ email, setEmail ] = useState('');
  const [ password, setPassword ] = useState('');
  const [ showPassword, setShowPassword ] = useState(false);

  const { message } = useSelector(state => state.message)
  const dispatch = useDispatch();

  useEffect(() => {
    emailRef.current.focus();
  }, []);

  useEffect(() => {
    clearMessage();
  }, [email, password])

  const handleSubmit = async (e) => {
     e.preventDefault();
    
    dispatch(login(email, password))
      .then(() => {
        navigate('/');
      })
  }

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container>
        <Grid item xs={12}>
          <h2 className='p-1 m-1 text-center'>Sign In to StatComplete</h2>
        </Grid>
      </Grid>
      <Grid container>
        <Grid item xs={12}>
          <Error errorRef={errorRef} message={message} />
        </Grid>
      </Grid>
      <Grid container className='justify-content-center'> 
        <Grid item xs={6}>
          <Box
            component='form'
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
                />
              </Grid>
            </Grid>
            <Grid container className='p-2 justify-content-center'>
              <Grid item xs={12}>
                <FormControl required variant='outlined' fullWidth>
                  <InputLabel htmlFor='password-input'>Password</InputLabel>
                  <OutlinedInput
                    id='password-input'
                    type={ showPassword ? 'text' : 'password'}
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    endAdornment={
                      <InputAdornment position='end'>
                        <IconButton
                          aria-label='toggle password visibility'
                          onClick={handleClickShowPassword}
                          onMouseDown={handleMouseDownPassword}
                          edge='end'
                        >
                          { showPassword ? <VisibilityOff /> : <Visibility /> }
                        </IconButton>
                      </InputAdornment>
                    }
                    label='Password'
                  />
                </FormControl>
              </Grid>
            </Grid>
            <Grid container className='p-2'>
              <Grid item xs={6}>
                <Button 
                  type='submit' 
                  color='primary' 
                  variant='contained'
                  disableElevation
                  disabled={email === '' || password === ''}
                  onClick={handleSubmit}
                >
                  Sign In
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
            Don't have an Account?
            <br/>
            <Button 
              color='primary'
              variant='contained'
              disableElevation
              href='/register'
              className='my-1 register-link-btn'
            >
              Register Here
            </Button>
          </p>
        </Grid>
      </Grid>
    </Box>
  );
}