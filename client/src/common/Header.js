import React, { Component } from 'react';
import {
  Col, 
  Container, 
  Row
} from 'reactstrap';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';

export default class Header extends Component {
  render() {
    return (
      <Container fluid className='p-0'>
        <Row className='p-2 align-items-center'>
          <Col className='m-2 text-left'>
            <h1>StatComplete</h1>
          </Col>
          <Col className='m-2 text-end'>
            <Link to='/' className='btn btn-secondary'>Sign In</Link>
          </Col>
        </Row>
        <Navbar/>
      </Container>
    );
  }
}