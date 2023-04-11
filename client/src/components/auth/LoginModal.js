import { Modal, Box } from '@mui/material';
import { CgProfile } from 'react-icons/cg'
import React, { Fragment, useState, useRef, useEffect } from 'react';
import { Button, Col, Form, FormGroup, Input, Label, Row } from 'reactstrap';
import axios from 'axios';

import './LoginModal.css'

const LOGIN_URL = 'login/';

const style = {
  position: 'absolute',
  top: '25%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

const LoginModal = () => {
  const usernameRef = useRef();
  const errorRef = useRef();

  const [ modalActive, setModalActive ] = useState(false);
  const [ username, setUsername ] = useState('');
  const [ password, setPassword ] = useState('');
  const [ errorMsg, setErrorMsg ] = useState('');

  useEffect(() => {
    if (modalActive) {
      usernameRef.current.focus();
    }
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
      // TODO: store the access token received here
      setModalActive(false);
    } catch (err) {
      if (!err?.response) {
        setErrorMsg('No server response');
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
    <Fragment>
      <Button
        className='sign-in-button p-0 m-0'
        onClick={() => setModalActive(true)}
      >
        <CgProfile className='profile-icon' />
      </Button>
      <Modal
        open={modalActive}
        onClose={() => setModalActive(false)}
        aria-labelledby='login-modal-title'
      >
        <Box sx={style}>
          <div ref={errorRef} className={errorMsg ? 'errorMsg' : 'offscreen'}
            aria-live='assertive'>
              {errorMsg}
          </div>
          <h2 id='login-modal-title'>Sign In to StatComplete</h2>
          <Form onSubmit={() => handleSubmit()}>
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
            <FormGroup row>
              <Col>
                <Button className='btn-danger' onClick={() => setModalActive(false)}>
                  Close
                </Button>
              </Col>
              <Col className='text-end'>
                <Button type='submit' color='primary'>
                  Sign In
                </Button>
              </Col>
            </FormGroup>
          </Form>
          <Row>
            <Col className='text-center'>
              <p>Don't have an Account?</p>
              <Button color='primary' onClick={() => setModalActive(false)}>
                Sign Up
              </Button>
            </Col>
          </Row>
        </Box>
      </Modal>
    </Fragment>
  );
}

export default LoginModal;
