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

export default function Register() {
  const navigate = useNavigate();

  const firstNameRef = useRef();
  const errorRef = useRef();

  const [ username, setUsername ] = useState('');
  const [ firstName, setFirstName ] = useState('');
  const [ lastName, setLastName ] = useState('');
  const [ email, setEmail ] = useState('');
  const [ password, setPassword ] = useState('');
  const [ confirmPassword, setConfirmPassword ] = useState('');
  const [ errorMsg, setErrorMsg ] = useState('');

  useEffect(() => {
    firstNameRef.current.focus();
  }, []);

  useEffect(() => {
    setErrorMsg('');
  }, [firstName, lastName, username, email, password, confirmPassword])

  const validatePassword = (formErrors) => {
    if (password !== '' && confirmPassword !== '') {
      if (password !== confirmPassword) {
        formErrors.push('Passwords must match.')
      }
    } else {
      formErrors.push('Passwords cannot be empty.')
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    let formErrors = [];
    validatePassword(formErrors);

    if (formErrors.length > 0) {
      let errorStr = '';
      formErrors.forEach((error) => {
        errorStr += error + '\n';
      })
      setErrorMsg(errorStr);
      errorRef.current.focus();
      return;
    }

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
      <div>
        <h2 className='p-1 m-1 text-center'>New StatComplete Account</h2>
      </div>
      <div ref={errorRef} className={errorMsg ? 'error-msg' : 'offscreen'}
        aria-live='assertive'>
          {errorMsg}
      </div>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for='usernameInput'>Username</Label>
          <Input
            id='username'
            type='text'
            placeholder='e.g. JSmith'
            onChange={(e) => setUsername(e.target.value)}
            value={username}
            required
          />
        </FormGroup>
        <FormGroup>
          <Label for='firstNameInput'>First Name</Label>
          <Input
            id='firstNameInput'
            type='text'
            ref={firstNameRef}
            placeholder='e.g. John'
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
            placeholder='e.g. Smith'
            onChange={(e) => setLastName(e.target.value)}
            value={lastName}
            required
          />
        </FormGroup>
        <FormGroup>
          <Label for='emailInput'>Email</Label>
          <Input
            id='emailInput'
            type='text'
            placeholder='e.g. john.smith@email.com'
            onChange={(e) => setEmail(e.target.value)}
            value={email}
            required
          />
        </FormGroup>
        <FormGroup>
          <Label for='passwordInput'>Password</Label>
          <Input
            id='passwordInput'
            type='password'
            onChange={(e) => setPassword(e.target.value)}
            value={password}
          />
        </FormGroup>
        <FormGroup>
          <Label for='confirmPassword'>Confirm Password</Label>
          <Input
            id='confirmPassword'
            type='password'
            onChange={(e) => setConfirmPassword(e.target.value)}
            value={confirmPassword}
          />
          <FormFeedback>
            These passwords must match.
          </FormFeedback>
        </FormGroup>
        <Button type='submit' color='primary'>
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