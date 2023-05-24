import { useState, useRef, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  Button,
  Container,
  Form,
  FormGroup,
  Input,
  Label,
  Row,
  Col,
  FormFeedback
} from 'reactstrap';
import { useDispatch, useSelector } from 'react-redux';

import './index.css';
import { publicAxios } from 'src/api/axios';
import { register } from 'src/state/token/actions';
import { clearMessage } from 'src/state/message/actions';

const CHECK_EMAIL_URL = 'check_email/'
const MINIMUM_PASSWORD_LENGTH = 7;
const REQUIRED_FIELD_MESSAGE = 'This field is required.';

export default function Register() {
  const navigate = useNavigate();

  const firstNameRef = useRef();
  const errorRef = useRef();

  const [ firstName, setFirstName ] = useState('');
  const [ firstNameErrorMsg, setFirstNameErrorMsg ] = useState('');
  const [ middleName, setMiddleName ] = useState('');
  const [ lastName, setLastName ] = useState('');
  const [ lastNameErrorMsg, setLastNameErrorMsg ] = useState('');
  const [ suffix, setSuffix ] = useState('');
  const [ email, setEmail ] = useState('');
  const [ emailErrorMsg, setEmailErrorMsg ] = useState('')
  const [ password, setPassword ] = useState('');
  const [ passwordErrorMsg, setPasswordErrorMsg ] = useState('')
  const [ confirmPassword, setConfirmPassword ] = useState('');
  const [ confirmPasswordErrorMsg, setConfirmPasswordErrorMsg ] = useState('')
  
  const { message } = useSelector(state => state.message);
  const dispatch = useDispatch();

  useEffect(() => {
    firstNameRef.current.focus();
  }, []);

  useEffect(() => {
    clearMessage();
  }, [firstName, middleName, lastName, suffix, email, password, confirmPassword])

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

    if (email !== '') {
      let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (re.test(email)) {
        setEmailErrorMsg('');
        checkEmail();
      } else {
        setEmailErrorMsg('Invalid email format.');
      }
    } else {
      setEmailErrorMsg(REQUIRED_FIELD_MESSAGE);
    }
  }, [email]);

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
    if (password !== '' || confirmPassword !== '') {
      if (password.length < MINIMUM_PASSWORD_LENGTH) {
        setPasswordErrorMsg(`Password must be at least ${MINIMUM_PASSWORD_LENGTH} characters long.`)
      } else if (password !== confirmPassword) {
        setPasswordErrorMsg('Passwords must match.')
      } else {
        setPasswordErrorMsg('');
      }
      if (password !== confirmPassword) {
        setConfirmPasswordErrorMsg('Passwords must match.')
      } else {
        setConfirmPasswordErrorMsg('');
      }
    } else {
      setPasswordErrorMsg(REQUIRED_FIELD_MESSAGE);
      setConfirmPasswordErrorMsg(REQUIRED_FIELD_MESSAGE);
    }
  }, [password, confirmPassword]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userRegistrationData = {
      first_name: firstName,
      last_name: lastName,
      email: email,
      password: password,
    }

    if (middleName !== '') {
      userRegistrationData['middle_name'] = middleName;
    }

    if (suffix !== '') {
      userRegistrationData['suffix'] = suffix;
    }

    dispatch(register(userRegistrationData))
      .then(() => {
        navigate('/');
      });
  }

  return (
    <Container className='p-2'>
      <Row>
        <Col>
          <h2 className='p-1 m-1 text-center'>New StatComplete Account</h2>
        </Col>
      </Row>
      <Row>
        <Col>
          <div ref={errorRef} className={message ? 'error-msg' : 'offscreen'}
            aria-live='assertive'>
              {message}
          </div>
        </Col>
      </Row>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for='emailInput'>Email</Label>
          <Input
            id='emailInput'
            type='email'
            placeholder='e.g. user@statcomplete.com'
            onChange={(e) => setEmail(e.target.value)}
            value={email}
            valid={emailErrorMsg === ''}
            invalid={emailErrorMsg !== ''}
            required
          />
          <FormFeedback>{emailErrorMsg}</FormFeedback>
        </FormGroup>
        <FormGroup>
          <Label for='firstNameInput'>First Name</Label>
          <Input
            id='firstNameInput'
            type='text'
            ref={firstNameRef}
            onChange={(e) => setFirstName(e.target.value)}
            valid={firstNameErrorMsg === ''}
            invalid={firstNameErrorMsg !== ''}
            value={firstName}
            required
          />
          <FormFeedback>{firstNameErrorMsg}</FormFeedback>
        </FormGroup>
        <FormGroup>
          <Label for='middleNameInput'>Middle Name</Label>
          <Input
            id='middleNameInput'
            type='text'
            onChange={(e) => setMiddleName(e.target.value)}
            valid={middleName !== ''}
            value={middleName}
          />
        </FormGroup>
        <FormGroup>
          <Label for='lastNameInput'>Last Name</Label>
          <Input
            id='lastNameInput'
            type='text'
            onChange={(e) => setLastName(e.target.value)}
            valid={lastNameErrorMsg === ''}
            invalid={lastNameErrorMsg !== ''}
            value={lastName}
            required
          />
          <FormFeedback>{lastNameErrorMsg}</FormFeedback>
        </FormGroup>
        <FormGroup>
          <Label for='suffixInput'>Suffix</Label>
          <Input
            id='suffixInput'
            type='text'
            onChange={(e) => setSuffix(e.target.value)}
            valid={suffix !== ''}
            value={suffix}
          />
        </FormGroup>
        <FormGroup>
          <Label for='passwordInput'>Password</Label>
          <Input
            id='passwordInput'
            type='password'
            onChange={(e) => setPassword(e.target.value)}
            value={password}
            valid={passwordErrorMsg === ''}
            invalid={passwordErrorMsg !== ''}
          />
          <FormFeedback>{passwordErrorMsg}</FormFeedback>
        </FormGroup>
        <FormGroup>
          <Label for='confirmPassword'>Confirm Password</Label>
          <Input
            id='confirmPassword'
            type='password'
            onChange={(e) => setConfirmPassword(e.target.value)}
            value={confirmPassword}
            valid={confirmPasswordErrorMsg === ''}
            invalid={confirmPasswordErrorMsg !== ''}
          />
          <FormFeedback>{confirmPasswordErrorMsg}</FormFeedback>
        </FormGroup>
        <Button
          className='btn btn-primary'
          color='primary'
          type='submit'
          disabled={
            firstName === '' || lastName === '' ||
            password === '' || passwordErrorMsg !== '' ||
            email === '' || emailErrorMsg !== '' ||
            confirmPassword === '' || confirmPasswordErrorMsg !== ''
          }
        >
          Register
        </Button>
        <div className='btn btn-danger float-end' onClick={() => navigate('/')}>
          Cancel
        </div>
      </Form>
      <Row>
        <Col className='text-center'>
          <p>
            Already have an Account?
            <br/>
            <Link className='btn btn-secondary register-link' to='/login'>Sign In Here</Link>
          </p>
        </Col>
      </Row>
    </Container>
  );
}