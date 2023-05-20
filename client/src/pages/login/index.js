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
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import './index.css';
import { login } from '../../state/token/actions';
import { clearMessage } from '../../state/message/actions';


export default function Login() {
  const navigate = useNavigate();

  const errorRef = useRef();
  const usernameRef = useRef();

  const [ username, setUsername ] = useState('');
  const [ password, setPassword ] = useState('');

  const { message } = useSelector(state => state.message)
  const dispatch = useDispatch();

  useEffect(() => {
    usernameRef.current.focus();
  }, []);

  useEffect(() => {
    clearMessage();
  }, [username, password])

  const handleSubmit = async (e) => {
     e.preventDefault();
    
    dispatch(login(username, password))
      .then(() => {
        navigate('/');
      })
  }

  return (
    <Container className='p-2'>
      <div>
        <h2 className='p-1 m-1 text-center'>Sign In to StatComplete</h2>
      </div>
      <div ref={errorRef} className={message ? 'error-msg' : 'offscreen'}
        aria-live='assertive'>
          {message}
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
          color='primary'
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