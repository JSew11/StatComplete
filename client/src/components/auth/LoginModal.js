import { Modal, Box } from '@mui/material';
import { CgProfile } from 'react-icons/cg'
import React, { Fragment, useState, useContext } from 'react';
import { Button, Col, Form, FormGroup, Input, Label, Row } from 'reactstrap';
import axios from 'axios';

import AuthContext from '../../context/AuthProvider';
import './LoginModal.css'

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

export default function LoginModal() {
  const [ modalActive, setModalActive ] = useState(false);
  const { setAuth } = useContext(AuthContext);
  const [ username, setUsername ] = useState('');
  const [ password, setPassword ] = useState('');

  const handleSubmit = async (e) => {
     e.preventDefault();
    
    try {
      const response = await axios.post(
        'login/',
        JSON.stringify({ username, password }),
        {
          headers: {'Content-Type': 'application/json'},
          withCredentials: true,
        }
      );
      const accessToken = response?.data?.access;
      setAuth({ username, password, accessToken });
    } catch (err) {
      console.log(err);
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
          <h2 id='login-modal-title'>Sign In to StatComplete</h2>
          <Form onSubmit={() => handleSubmit()}>
            <FormGroup floating>
              <Input 
                id='usernameInput' 
                type='text'
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
                <Button color='primary'>
                  Sign In
                </Button>
              </Col>
            </FormGroup>
          </Form>
          <Row>
            <Col className='text-center'>
              <p>Don't have an Account?</p>
              <Button color='primary' onClick={() => setModalActive(false)}>Sign Up</Button>
            </Col>
          </Row>
        </Box>
      </Modal>
    </Fragment>
  );
}
