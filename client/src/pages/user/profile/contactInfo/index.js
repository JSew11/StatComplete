import { useEffect, useState } from 'react';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';

import { publicAxios } from 'src/api/axios';

const CHECK_EMAIL_URL = 'check_email/';
const REQUIRED_FIELD_MESSAGE = 'This field is required.';

export default function ContactInfo({ user }) {
  const [ editingContactInfo, setEditingContactInfo ] = useState(false);
  const [ prevEmail, setPrevEmail ] = useState(user.email ?? '');
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
      if (email !== prevEmail) {
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
      } else {
        setEmailErrorMsg('');
      }
    }, 1000);

    return () => {
      setEmailErrorMsg('Validating email.')
      clearTimeout(delayCheckEmail);
    };
  }, [email]);

  return (
    <Card elevation={0}>
      <CardHeader title='Contact Info' />
      <CardContent>
        <Box component='form' sx={{ flexGrow: 1 }} className='m-2'>
          <Grid container>
            <Grid item xs={5} className='m-2'>
              <TextField
                required={editingContactInfo}
                type='text'
                label='Email'
                variant='outlined'
                size='small'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                fullWidth
                InputProps={{ readOnly: !editingContactInfo }}
                InputLabelProps={{ shrink: true }}
                helperText={emailErrorMsg}
              />
            </Grid>
          </Grid>
        </Box>
      </CardContent>
    </Card>
  );
}