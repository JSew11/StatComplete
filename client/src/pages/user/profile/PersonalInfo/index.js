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

import './index.css';
import { useEffect, useState } from 'react';

import { publicAxios } from 'src/api/axios';

const CHECK_EMAIL_URL = 'check_email/';
const REQUIRED_FIELD_MESSAGE = 'This field is required.';

export default function PersonalInfo() {
  const [ editingPersonalInfo, setEditingPersonalInfo ] = useState(false);
  const [ prevFirstName, setPrevFirstName ] = useState('');
  const [ firstName, setFirstName ] = useState('');
  const [ firstNameErrorMsg, setFirstNameErrorMsg ] = useState('');
  const [ prevMiddleName, setPrevMiddleName ] = useState('');
  const [ middleName, setMiddleName ] = useState('');
  const [ prevLastName, setPrevLastName ] = useState('');
  const [ lastName, setLastName ] = useState('');
  const [ lastNameErrorMsg, setLastNameErrorMsg ] = useState('');
  const [ prevSuffix, setPrevSuffix ] = useState('');
  const [ suffix, setSuffix ] = useState('');
  const [ prevEmail, setPrevEmail ] = useState('');
  const [ email, setEmail ] = useState('');
  const [ emailErrorMsg, setEmailErrorMsg ] = useState('');

  const restorePersonalInfo = () => {
    setFirstName(prevFirstName);
    setMiddleName(prevMiddleName);
    setLastName(prevLastName);
    setSuffix(prevSuffix);
    setEmail(prevEmail);
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

  useEffect(() => {
    const checkEmail = async () => {
      try {
        const response = await publicAxios.post(
          CHECK_EMAIL_URL,
          JSON.stringify({
            email: email,
          })
        );
        if (response?.data?.email_available) {
          setEmailErrorMsg('');
        } else {
          setEmailErrorMsg('This email is not available.');
        }
      } catch (err) {
        setEmailErrorMsg('Could not determine if email is available. Please try again later.')
      }
    }

    const delayCheckEmail = setTimeout(() => {
      if (email !== '') {
        let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (re.test(email)) {
          checkEmail();
        } else {
          setEmailErrorMsg('Invalid email format.');
        }
      } else {
        setEmailErrorMsg(REQUIRED_FIELD_MESSAGE);
      }
    }, 1000);

    return () => {
      setEmailErrorMsg('Validating email.')
      clearTimeout(delayCheckEmail);
    };
  }, [email]);

  const savePersonalInfo = async (e) => {
    e.preventDefault();

    if (editingPersonalInfo) {
      // TODO: send the edit user request
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
      if (email !== prevEmail) {
        updated_fields['email'] = email;
      }
      console.log(updated_fields);
    }
    setPrevFirstName(firstName);
    setPrevMiddleName(middleName);
    setPrevLastName(lastName);
    setPrevSuffix(suffix);
    setPrevEmail(email);
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
                valid={middleName !== ''}
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
                valid={suffix !== ''}
                onChange={(e) => setSuffix(e.target.value)}
                disabled={!editingPersonalInfo}
              />
            </Col>
          </FormGroup>
          <FormGroup row>
            <Col className='col-5'>
              <Label for='emailInput'>Email</Label>
              <Input
                id='emailInput'
                type='email'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                valid={editingPersonalInfo && emailErrorMsg === ''}
                invalid={editingPersonalInfo && emailErrorMsg !== ''}
                disabled={!editingPersonalInfo}
              />
              <FormFeedback>{emailErrorMsg}</FormFeedback>
            </Col>
          </FormGroup>
          <Button 
            className='m-1'
            disabled={
              editingPersonalInfo &&
              emailErrorMsg !== '' && firstNameErrorMsg !== '' &&
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