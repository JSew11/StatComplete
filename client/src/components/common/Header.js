import React, { Component } from 'react';
import {
  Col, 
  Container, 
  Row
} from 'reactstrap';
import LoginForm from '../auth/LoginForm';
import Navbar from './Navbar';

export default class Header extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Container fluid>
        <Row className='p-2 align-items-center'>
          <Col className='text-left'>
            <h1>StatComplete</h1>
          </Col>
          <Col className='text-end'>
            <LoginForm />
          </Col>
        </Row>
        <Row>
          <Navbar />
        </Row>
      </Container>
    );
  }
}