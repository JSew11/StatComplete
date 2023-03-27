import React, { Component } from 'react';
import {
  Col, 
  Container, 
  Row
} from 'reactstrap';
import LoginModal from '../auth/LoginModal';
import Navbar from './Navbar';

export default class Header extends Component {
  render() {
    return (
      <Container fluid>
        <Row className='p-2 align-items-center'>
          <Col className='text-left'>
            <h1>StatComplete</h1>
          </Col>
          <Col className='text-end'>
            <LoginModal />
          </Col>
        </Row>
        <Row>
          <Navbar />
        </Row>
      </Container>
    );
  }
}