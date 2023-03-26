import { Modal } from '@mui/material';
import React, { Component } from 'react';

export default class RegisterUser extends Component {
  constructor(props) {
    super(props);
    this.state = {
      'showModal': false,
    };
  }

  render() {
    return (
      <Modal open={this.state.showModal}>
        Register
      </Modal>
    );
  }
}