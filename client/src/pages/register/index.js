import { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container } from 'reactstrap';
import axios from 'axios';

const REGISTER_URL = 'register/';

export default function Register() {
  const navigate = useNavigate();

  const firstNameRef = useRef();
  const errorRef = useRef();

  const [ firstName, setFirstName ] = useState('');
  const [ lastName, setLastName ] = useState('');
  const [ username, setUsername ] = useState('');
  const [ email, setEmail ] = useState('');
  const [ password, setPassword ] = useState('');
  const [ confirmPassword, setConfirmPassword ] = useState('');
  const [ errorMsg, setErrorMsg ] = useState('');

  useEffect(() => {
    // firstNameRef.current.focus();
  }, []);

  useEffect(() => {
    setErrorMsg('');
  }, [firstName, lastName, username, email, password, confirmPassword])

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        REGISTER_URL,
        JSON.stringify({
          first_name: firstName,
          last_name: lastName,
          username: username,
          email: email,
          password: password 
        }),
        {
          headers: {
            'Content-Type': 'application/json',
          },
          withCredentials: true
        }
      );
      // TODO: get the accessToken and store it in localStorage
      navigate('/login'); // TODO
    } catch (err) {
      if (!err?.response) {
        setErrorMsg('No Server Response');
      } else if (err.response?.status === 400) {
        setErrorMsg('Missing Information');
      } else if (err.response?.status === 401) {
        setErrorMsg('Unauthorized');
      } else {
        setErrorMsg('Registration Failed');
      }
      // errorRef.current.focus();
    }
  }

  return (
    <Container>
      <h1>Register</h1>
    </Container>
  );
}