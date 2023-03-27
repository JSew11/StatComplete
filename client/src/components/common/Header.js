import React, { Component } from 'react';
import {
  Col, 
  Container, 
  Row
} from 'reactstrap';
import LoginUser from '../auth/LoginUser';

export default class Header extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Container fluid className='p-0'>
        <Row className='p-2 align-items-center'>
          <Col className='text-left'>
            <h1>StatComplete</h1>
          </Col>
          <Col className='text-end'>
            <LoginUser />
          </Col>
        </Row>
      </Container>
    );
  }
}