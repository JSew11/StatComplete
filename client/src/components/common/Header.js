import React, { Component } from 'react';
import {
  Col, 
  Container, 
  Row
} from 'reactstrap';
import LoginUser from '../auth/LoginUser';
import Navbar from './Navbar';

export default class Header extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Container fluid className='p-0'>
        <Row className='p-2 align-items-center'>
          <Col className='m-2 text-left'>
            <h1>StatComplete</h1>
          </Col>
          <Col className='m-2 text-end'>
            <LoginUser />
          </Col>
        </Row>
        <Row>
          <Navbar/>
        </Row>
      </Container>
    );
  }
}