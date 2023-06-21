import { useEffect, useState } from 'react';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

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
      UserApi.partialUpdateUser(user.id, updated_fields);
    }
    setPrevFirstName(firstName);
    setPrevMiddleName(middleName);
    setPrevLastName(lastName);
    setPrevSuffix(suffix);
    setEditingPersonalInfo(!editingPersonalInfo);
  };

  return (
    <Card elevation={0}>
      <CardHeader title='Personal Info' />
      <CardContent>
        <Box component='form' sx={{ flexGrow: 1 }} className='m-2'>
          <Grid container>
            <Grid item xs={3} className='m-2'>
              <TextField
                required={editingPersonalInfo}
                type='text'
                label='First Name'
                variant='outlined'
                size='small'
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                fullWidth
                InputProps={{ readOnly: !editingPersonalInfo }}
                InputLabelProps={{ shrink: true }}
                error={firstNameErrorMsg !== ''}
                helperText={firstNameErrorMsg}
              />
            </Grid>
            <Grid item xs={3} className='m-2'>
              <TextField
                type='text'
                label='Middle Name'
                variant='outlined'
                size='small'
                value={middleName}
                onChange={(e) => setMiddleName(e.target.value)}
                fullWidth
                InputProps={{ readOnly: !editingPersonalInfo }}
                InputLabelProps={{ shrink: true }}
              />
            </Grid>
            <Grid item xs={3} className='m-2'>
              <TextField
                required={editingPersonalInfo}
                type='text'
                label='Last Name'
                variant='outlined'
                size='small'
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                fullWidth
                InputProps={{ readOnly: !editingPersonalInfo }}
                InputLabelProps={{ shrink: true }}
                error={lastNameErrorMsg !== ''}
                helperText={lastNameErrorMsg}
              />
            </Grid>
            <Grid item xs={1} className='m-2'>
              <TextField 
                type='text'
                label='Suffix'
                variant='outlined'
                size='small'
                value={suffix}
                onChange={(e) => setSuffix(e.target.value)}
                fullWidth
                InputProps={{ readOnly: !editingPersonalInfo }}
                InputLabelProps={{ shrink: true }}
              />
            </Grid>
          </Grid>
          <Grid container>
            <Grid item className='m-2'>
              <Button 
                variant='contained'
                disableElevation
                onClick={savePersonalInfo}
                disabled={
                  editingPersonalInfo &&
                  (firstName === '' || lastName === '')
                }
              >
                { editingPersonalInfo ? 'Save' : 'Edit' }
              </Button>
            </Grid>
              { 
                editingPersonalInfo 
                &&
                <Grid item className='m-2'>
                  <Button
                    variant='contained'
                    color='error'
                    disableElevation
                    onClick={restorePersonalInfo}
                  >
                    Cancel
                  </Button>
                </Grid>
              }
          </Grid>
        </Box>
      </CardContent>
    </Card>
  );
}