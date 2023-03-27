import React, { Component } from 'react';
import {
  Col, 
  Container, 
  Row
} from 'reactstrap';

export default class Footer extends Component {
  render() {
    return (
      <Container fluid className='footer p-0'>
        <Row className='p-2'>
          <Col>
            Footer
          </Col>
        </Row>
      </Container>
    );
  }
}