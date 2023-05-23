import {
  Card,
  CardBody,
  CardHeader,
  Form,
  FormGroup,
  Input,
  Label,
  Col,
  Button,
} from 'reactstrap';

import './index.css';
import { useState } from 'react';

export default function PersonalInfo() {
  const [ editingPersonalInfo, setEditingPersonalInfo ] = useState(false);

  const restorePersonalInfo = () => {
    // TODO: restore old values for personal info
    setEditingPersonalInfo(!editingPersonalInfo);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (editingPersonalInfo) {
      // TODO: send the edit user request
    }
    setEditingPersonalInfo(!editingPersonalInfo);
  };

  return (
    <Card>
      <CardHeader>
        Personal Info
      </CardHeader>
      <CardBody>
        <Form onSubmit={handleSubmit}>
          <FormGroup row>
            <Col className='col-3'>
              <Label for='firstNameInput'>First Name</Label>
              <Input 
                id='firstNameInput'
                type='text'
                disabled={!editingPersonalInfo}
              />
            </Col>
            <Col className='col-3'>
              <Label for='middleNameInput'>Middle Name</Label>
              <Input 
                id='middleNameInput'
                type='text'
                disabled={!editingPersonalInfo}
              />
            </Col>
            <Col className='col-3'>
              <Label for='lastNameInput'>Last Name</Label>
              <Input 
                id='lastNameInput'
                type='text'
                disabled={!editingPersonalInfo}
              />
            </Col>
            <Col className='col-2'>
              <Label for='suffixInput'>Suffix</Label>
              <Input 
                id='suffixInput'
                type='text'
                disabled={!editingPersonalInfo}
              />
            </Col>
          </FormGroup>
          <FormGroup row>
            <Col className='col-4'>
              <Label for='emailInput'>Email</Label>
              <Input
                id='emailInput'
                type='email'
                disabled={!editingPersonalInfo}
              />
            </Col>
          </FormGroup>
          <Button className='m-1'>{editingPersonalInfo ? 'Save' : 'Edit'}</Button>
          { 
            editingPersonalInfo &&
            <div className='btn btn-danger m-1' onClick={restorePersonalInfo}>
              Cancel
            </div>
          }
        </Form>
      </CardBody>
    </Card>
  );
}