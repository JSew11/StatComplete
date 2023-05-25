import {
  Row,
  Col,
  Spinner,
} from 'reactstrap';

import './index.css';

export default function Loading() {
  return (
    <>
      <Row className='p-2 align-items-center'>
        <Col className='text-center'><Spinner className='loading-spinner' /></Col>
      </Row>
      <Row className='p-2 align-items-center'>
        <Col className='text-center'><h4 className='loading-text'>Loading</h4></Col>
      </Row>
    </>
  );
}