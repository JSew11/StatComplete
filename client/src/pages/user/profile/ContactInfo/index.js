import { useEffect, useState } from 'react';
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

import { publicAxios } from 'src/api/axios';

const CHECK_EMAIL_URL = 'check_email/';
const REQUIRED_FIELD_MESSAGE = 'This field is required.';

export default function ContactInfo({ user }) {
  const [ editingContactInfo, setEditingContactInfo ] = useState(false);
  const [ prevEmail, setPrevEmail ] = useState('');
  const [ email, setEmail ] = useState(user.email ?? '');
  const [ emailErrorMsg, setEmailErrorMsg ] = useState('');

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
      if (email !== '' || email !== prevEmail) {
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

  return (
    <Card>
      <CardHeader>Contact Info</CardHeader>
      <CardBody>
        <Form>
          <FormGroup row>
            <Col className='col-5'>
              <Label for='emailInput'>Email</Label>
              <Input
                id='emailInput'
                type='email'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                valid={editingContactInfo && emailErrorMsg === ''}
                invalid={editingContactInfo && emailErrorMsg !== ''}
                disabled={!editingContactInfo}
              />
              <FormFeedback>{emailErrorMsg}</FormFeedback>
            </Col>
          </FormGroup>
        </Form>
      </CardBody>
    </Card>
  )
}