import { Modal, Box } from '@mui/material';
import { CgProfile } from 'react-icons/cg'
import React, { Component, Fragment } from 'react';
import { Button, Col, Form, FormGroup, Input, Label, Row } from 'reactstrap';
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

export default class LoginModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      'modalShowing': false,
    };
  }

  showModal = () => {
    this.setState({
      'modalShowing': true
    });
  }

  hideModal = () => {
    this.setState({
      'modalShowing': false
    });
  }

  handleSubmit = () => {
    console.log('Login User')
  }

  render() {
    return (
      <Fragment>
        <Button onClick={this.showModal} className='sign-in-button p-0 m-0'>
          <CgProfile className='profile-icon' />
        </Button>
        <Modal
          open={this.state.modalShowing}
          onClose={this.hideModal}
          aria-labelledby='login-modal-title'
        >
          <Box sx={style}>
            <h2 id='login-modal-title'>Sign In to StatComplete</h2>
            <Form onSubmit={this.handleSubmit}>
              <FormGroup floating>
                <Input id='usernameInput' type='text'
                  placeholder='Username'/>
                <Label for='usernameInput'>Username</Label>
              </FormGroup>
              <FormGroup floating>
                <Input id='passwordInput' type='password'
                  placeholder='Password'/>
                <Label for='passwordInput'>Password</Label>
              </FormGroup>
              <FormGroup row>
                <Col>
                  <Button className='btn-danger' onClick={this.hideModal}>
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
                <Button color='primary' onClick={this.hideModal}>Sign Up</Button>
              </Col>
            </Row>
          </Box>
        </Modal>
      </Fragment>
    );
  }
}