import { useState, useRef, useEffect } from 'react';
import {
  Container,
  Row,
  Col,
  Form,
  FormGroup,
  Label,
  Input,
  Button,
} from 'reactstrap';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

const LOGIN_URL = 'login/';

export default function Login() {
  const navigate = useNavigate();

  const usernameRef = useRef();
  const errorRef = useRef();

  const [ username, setUsername ] = useState('');
  const [ password, setPassword ] = useState('');
  const [ errorMsg, setErrorMsg ] = useState('');

  useEffect(() => {
      usernameRef.current.focus();
  }, [])
  
  useEffect(() => {
    setErrorMsg('');
  }, [username, password])

  const handleSubmit = async (e) => {
     e.preventDefault();
    
    try {
      const response = await axios.post(
        LOGIN_URL,
        JSON.stringify({ username: username, password: password }),
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
      navigate(-1);
    } catch (err) {
      if (!err?.response) {
        setErrorMsg('No Server Response');
      } else if (err.response?.status === 400) {
        setErrorMsg('Missing Username or Password');
      } else if (err.response?.status === 401) {
        setErrorMsg('Unauthorized');
      } else {
        setErrorMsg('Login Failed');
      }
      errorRef.current.focus();
    }
  }

  return (
    <Container className='p-2'>
      <div>
        <h2 className='p-1 m-1 text-center'>Sign In to StatComplete</h2>
      </div>
      <div ref={errorRef} className={errorMsg ? 'errorMsg' : 'offscreen'}
        aria-live='assertive'>
          {errorMsg}
      </div>
      <Form onSubmit={handleSubmit}>
        <FormGroup floating>
          <Input 
            id='usernameInput' 
            type='text'
            ref={usernameRef}
            placeholder='Username'
            onChange={(e) => setUsername(e.target.value)}
            value={username}
            required
          />
          <Label for='usernameInput'>Username</Label>
        </FormGroup>
        <FormGroup floating>
          <Input 
            id='passwordInput'
            type='password'
            placeholder='Password'
            onChange={(e) => setPassword(e.target.value)}
            value={password}
            required
          />
          <Label for='passwordInput'>Password</Label>
        </FormGroup>
        <Button
          className='btn btn-primary'
          type='submit'
          disabled={username === '' || password === ''}
        >
          Sign In
        </Button>
        <div className='btn btn-danger float-end' onClick={() => {navigate('/')}}>
          Cancel
        </div>
      </Form>
      <Row>
        <Col className='text-center'>
          <p>
            Don't have an Account?
            <br/>
            <Link className='btn btn-secondary register-link' to='/register'>Register Here</Link>
          </p>
        </Col>
      </Row>
    </Container>
  );
}