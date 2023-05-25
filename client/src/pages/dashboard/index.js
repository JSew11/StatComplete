import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import {
  Container,
  Row,
  Col
} from 'reactstrap';

const Dashboard = () => {
  const [ tempVar, setTempVar ] = useState('');

  const { isLoggedIn } = useSelector(state => state.auth);

  useEffect(() => {
    if (isLoggedIn) {
      // TODO: call API to get user-specific dashboard data
      setTempVar('Logged In');
    } else {
      // TODO: call API to get generic dashboard data
      setTempVar('Not Logged In');
    }
  }, []);

  return (
    <Container fluid>
      <Row className='p-2'>
        <Col className='text-center'><h1>{tempVar}</h1></Col>
      </Row>
    </Container>
  );
}

export default Dashboard;