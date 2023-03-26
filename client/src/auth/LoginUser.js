import { Modal, Box } from '@mui/material';
import React, { Component, Fragment } from 'react';
import { Button } from 'reactstrap';

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

export default class LoginUser extends Component {
  constructor(props) {
    super(props);
    this.state = {
      'showModal': false,
    };
  }

  showModal = () => {
    this.setState({
      'showModal': true
    });
  }

  hideModal = () => {
    this.setState({
      'showModal': false
    });
  }

  render() {
    return (
      <Fragment>
        <Button onClick={this.showModal} className='btn btn-secondary'>Sign In</Button>
        <Modal
          open={this.state.showModal}
          onClose={this.hideModal}
          aria-labelledby='login-modal-title'
        >
          <Box sx={style}>
            <h2 id='login-modal-title'>Sign In to StatComplete</h2>
          </Box>
        </Modal>
      </Fragment>
    );
  }
}