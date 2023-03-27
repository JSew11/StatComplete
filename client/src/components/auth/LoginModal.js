import { Modal, Box } from '@mui/material';
import React, { Component, Fragment } from 'react';
import { Button, Col, Form, FormGroup, Input, Label, Row } from 'reactstrap';

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
        <Button onClick={this.showModal} className='btn btn-secondary'>Sign In</Button>
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
                  <Button className='sign-in-btn' >
                    Sign In
                  </Button>
                </Col>
              </FormGroup>
            </Form>
            <Row>
              <Col className='text-center'>
                <p>Don't have an Account?</p>
                <Button onClick={this.hideModal}>Sign Up</Button>
              </Col>
            </Row>
          </Box>
        </Modal>
      </Fragment>
    );
  }
}