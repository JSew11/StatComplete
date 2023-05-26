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
  FormFeedback,
} from 'reactstrap';
import { useEffect, useState } from 'react';

import UserApi from 'src/api/user';

const REQUIRED_FIELD_MESSAGE = 'This field is required.';

export default function PersonalInfo({ user }) {
  const [ editingPersonalInfo, setEditingPersonalInfo ] = useState(false);
  const [ prevFirstName, setPrevFirstName ] = useState('');
  const [ firstName, setFirstName ] = useState(user.first_name ?? '');
  const [ firstNameErrorMsg, setFirstNameErrorMsg ] = useState('');
  const [ prevMiddleName, setPrevMiddleName ] = useState('');
  const [ middleName, setMiddleName ] = useState(user.middle_name ?? '');
  const [ prevLastName, setPrevLastName ] = useState('');
  const [ lastName, setLastName ] = useState(user.last_name ?? '');
  const [ lastNameErrorMsg, setLastNameErrorMsg ] = useState('');
  const [ prevSuffix, setPrevSuffix ] = useState('');
  const [ suffix, setSuffix ] = useState(user.suffix ?? '');

  const restorePersonalInfo = () => {
    setFirstName(prevFirstName);
    setMiddleName(prevMiddleName);
    setLastName(prevLastName);
    setSuffix(prevSuffix);
    setEditingPersonalInfo(!editingPersonalInfo);
  };

  useEffect(() => {
    if (firstName !== '') {
      setFirstNameErrorMsg('');
    } else {
      setFirstNameErrorMsg(REQUIRED_FIELD_MESSAGE);
    }
  }, [firstName])

  useEffect(() => {
    if (lastName !== '') {
      setLastNameErrorMsg('');
    } else {
      setLastNameErrorMsg(REQUIRED_FIELD_MESSAGE);
    }
  }, [lastName])

  const savePersonalInfo = async (e) => {
    e.preventDefault();

    if (editingPersonalInfo) {
      const updated_fields = {};
      if (firstName !== prevFirstName) {
        updated_fields['first_name'] = firstName;
      }
      if (middleName !== prevMiddleName) {
        updated_fields['middle_name'] = middleName;
      }
      if (lastName !== prevLastName) {
        updated_fields['last_name'] = lastName;
      }
      if (suffix !== prevSuffix) {
        updated_fields['suffix'] = suffix;
      }
      UserApi.partial_update_user(user.id, updated_fields);
    }
    setPrevFirstName(firstName);
    setPrevMiddleName(middleName);
    setPrevLastName(lastName);
    setPrevSuffix(suffix);
    setEditingPersonalInfo(!editingPersonalInfo);
  };

  return (
    <Card>
      <CardHeader>
        Personal Info
      </CardHeader>
      <CardBody>
        <Form onSubmit={savePersonalInfo}>
          <FormGroup row>
            <Col className='col-3'>
              <Label for='firstNameInput'>First Name</Label>
              <Input 
                id='firstNameInput'
                type='text'
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                valid={editingPersonalInfo && firstNameErrorMsg === ''}
                invalid={editingPersonalInfo && firstNameErrorMsg !== ''}
                disabled={!editingPersonalInfo}
              />
              <FormFeedback>{firstNameErrorMsg}</FormFeedback>
            </Col>
            <Col className='col-3'>
              <Label for='middleNameInput'>Middle Name</Label>
              <Input 
                id='middleNameInput'
                type='text'
                value={middleName}
                valid={editingPersonalInfo && middleName !== ''}
                onChange={(e) => setMiddleName(e.target.value)}
                disabled={!editingPersonalInfo}
              />
            </Col>
            <Col className='col-3'>
              <Label for='lastNameInput'>Last Name</Label>
              <Input 
                id='lastNameInput'
                type='text'
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                valid={editingPersonalInfo && lastNameErrorMsg === ''}
                invalid={editingPersonalInfo && lastNameErrorMsg !== ''}
                disabled={!editingPersonalInfo}
              />
              <FormFeedback>{lastNameErrorMsg}</FormFeedback>
            </Col>
            <Col className='col-2'>
              <Label for='suffixInput'>Suffix</Label>
              <Input 
                id='suffixInput'
                type='text'
                value={suffix}
                valid={editingPersonalInfo && suffix !== ''}
                onChange={(e) => setSuffix(e.target.value)}
                disabled={!editingPersonalInfo}
              />
            </Col>
          </FormGroup>
          <Button 
            className='m-1'
            disabled={
              editingPersonalInfo &&
              firstNameErrorMsg !== '' &&
              lastNameErrorMsg !== ''
            }
          >
              {editingPersonalInfo ? 'Save' : 'Edit'}
          </Button>
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