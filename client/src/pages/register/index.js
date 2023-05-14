import { useState, useRef, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  Button,
  Container,
  Form,
  FormGroup,
  Input,
  Label,
  Row,
  Col,
  FormFeedback
} from 'reactstrap';
import axios from 'axios';

import './index.css';

const REGISTER_URL = 'register/';
const CHECK_USERNAME_URL = 'check_username/'
const CHECK_EMAIL_URL = 'check_email/'
const MINIMUM_PASSWORD_LENGTH = 7;

export default function Register() {
  const navigate = useNavigate();

  const firstNameRef = useRef();
  const errorRef = useRef();

  const [ username, setUsername ] = useState('');
  const [ usernameErrorMsg, setUsernameErrorMsg ] = useState('')
  const [ firstName, setFirstName ] = useState('');
  const [ lastName, setLastName ] = useState('');
  const [ email, setEmail ] = useState('');
  const [ emailErrorMsg, setEmailErrorMsg ] = useState('')
  const [ password, setPassword ] = useState('');
  const [ passwordErrorMsg, setPasswordErrorMsg ] = useState('')
  const [ confirmPassword, setConfirmPassword ] = useState('');
  const [ confirmPasswordErrorMsg, setConfirmPasswordErrorMsg ] = useState('')
  const [ errorMsg, setErrorMsg ] = useState('');

  useEffect(() => {
    firstNameRef.current.focus();
  }, []);

  useEffect(() => {
    setErrorMsg('');
  }, [firstName, lastName, username, email, password, confirmPassword])

  useEffect(() => {
    validatePassword()
  }, [password, confirmPassword])

  useEffect(() => {
    validateUsername()
  }, [username])

  useEffect(() => {
    validateEmail()
  }, [email])

  const validateUsername = async () => {
    if (username !== '') {
      let re = /^[A-Za-z][\w]{7,29}$/;
      if (re.test(username)) {
        setUsernameErrorMsg('');
        try {
          const response = await axios.post(
            CHECK_USERNAME_URL,
            JSON.stringify({
              username: username,
            }),
            {
              headers: {
                'Content-Type': 'application/json',
              },
              withCredentials: true
            }
          );
          if (response?.data?.username_available) {
            setUsernameErrorMsg('');
          } else {
            setUsernameErrorMsg('This username is not available.');
          }
        } catch (err) {
          setUsernameErrorMsg('Could not determine if username is available. Please try again later.')
        }
      } else {
        setUsernameErrorMsg('Username must be at least 8 characters and use only letters, numbers, and "_".')
      }
    } else {
      setUsernameErrorMsg('');
    }
  }

  const validateEmail = async () => {
    if (email !== '') {
      let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (re.test(email)) {
        setEmailErrorMsg('');
        try {
          const response = await axios.post(
            CHECK_EMAIL_URL,
            JSON.stringify({
              email: email,
            }),
            {
              headers: {
                'Content-Type': 'application/json',
              },
              withCredentials: true
            }
          );
          if (response?.data?.email_available) {
            setEmailErrorMsg('');
          } else {
            setEmailErrorMsg('This email is not available.');
          }
        } catch (err) {
          setEmailErrorMsg('Could not determine if email is available. Please try again later.')
        }
      } else {
        setEmailErrorMsg('Invalid email format.');
      }
    } else {
      setEmailErrorMsg('');
    }
  }

  const validatePassword = () => {
    if (password !== '' || confirmPassword != '') {
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
      setPasswordErrorMsg('');
      setConfirmPasswordErrorMsg('');
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        REGISTER_URL,
        JSON.stringify({
          first_name: firstName,
          last_name: lastName,
          username: username,
          email: email,
          password: password 
        }),
        {
          headers: {
            'Content-Type': 'application/json',
          },
          withCredentials: true
        }
      );
      const accessToken = response?.data?.access;
      // store token in localstorage
      localStorage.setItem('token', accessToken);
      axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;
      navigate('/');
    } catch (err) {
      if (!err?.response) {
        setErrorMsg('No Server Response');
      } else if (err.response?.status === 400) {
        setErrorMsg('Missing Information');
      } else if (err.response?.status === 401) {
        setErrorMsg('Unauthorized');
      } else {
        setErrorMsg('Registration Failed');
      }
      errorRef.current.focus();
    }
  }

  return (
    <Container className='p-2'>
      <Row>
        <Col>
          <h2 className='p-1 m-1 text-center'>New StatComplete Account</h2>
        </Col>
      </Row>
      <Row>
        <Col>
          <div ref={errorRef} className={errorMsg ? 'error-msg' : 'offscreen'}
            aria-live='assertive'>
              {errorMsg}
          </div>
        </Col>
      </Row>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for='usernameInput'>Username</Label>
          <Input
            id='username'
            type='text'
            placeholder='e.g. Score_Keeper1'
            onChange={(e) => setUsername(e.target.value)}
            value={username}
            valid={usernameErrorMsg === '' && username !== ''}
            invalid={usernameErrorMsg !== ''}
            required
          />
          <FormFeedback>{usernameErrorMsg}</FormFeedback>
        </FormGroup>
        <FormGroup>
          <Label for='firstNameInput'>First Name</Label>
          <Input
            id='firstNameInput'
            type='text'
            ref={firstNameRef}
            onChange={(e) => setFirstName(e.target.value)}
            value={firstName}
            required
          />
        </FormGroup>
        <FormGroup>
          <Label for='lastNameInput'>Last Name</Label>
          <Input
            id='lastNameInput'
            type='text'
            onChange={(e) => setLastName(e.target.value)}
            value={lastName}
            required
          />
        </FormGroup>
        <FormGroup>
          <Label for='emailInput'>Email</Label>
          <Input
            id='emailInput'
            type='email'
            placeholder='e.g. user@statcomplete.com'
            onChange={(e) => setEmail(e.target.value)}
            value={email}
            valid={emailErrorMsg === '' && email !== ''}
            invalid={emailErrorMsg !== ''}
            required
          />
          <FormFeedback>{emailErrorMsg}</FormFeedback>
        </FormGroup>
        <FormGroup>
          <Label for='passwordInput'>Password</Label>
          <Input
            id='passwordInput'
            type='password'
            onChange={(e) => setPassword(e.target.value)}
            value={password}
            valid={passwordErrorMsg === '' && password != ''}
            invalid={passwordErrorMsg != ''}
          />
          <FormFeedback>{passwordErrorMsg}</FormFeedback>
        </FormGroup>
        <FormGroup>
          <Label for='confirmPassword'>Confirm Password</Label>
          <Input
            id='confirmPassword'
            type='password'
            onChange={(e) => setConfirmPassword(e.target.value)}
            value={confirmPassword}
            valid={confirmPasswordErrorMsg === '' && confirmPassword != ''}
            invalid={confirmPasswordErrorMsg !== ''}
          />
          <FormFeedback>{confirmPasswordErrorMsg}</FormFeedback>
        </FormGroup>
        <Button
          type='submit'
          color='primary'
          disabled={
            username === '' || usernameErrorMsg !== '' ||
            firstName === '' || lastName === '' ||
            password === '' || passwordErrorMsg !== '' ||
            email === '' || emailErrorMsg !== '' ||
            confirmPassword === '' || confirmPasswordErrorMsg !== ''
          }
        >
          Register
        </Button>
        <div className='btn btn-danger float-end' onClick={() => navigate('/')}>
          Cancel
        </div>
      </Form>
      <Row>
        <Col className='text-center'>
          <p>
            Already have an Account?
            <br/>
            <Link className='btn btn-secondary register-link' to='/login'>Sign In Here</Link>
          </p>
        </Col>
      </Row>
    </Container>
  );
}