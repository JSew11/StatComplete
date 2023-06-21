import { useEffect, useState } from 'react';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

import OrganizationApi from 'src/api/organization';
import Loading from 'src/components/loading';

const REQUIRED_FIELD_MESSAGE = 'This field is required.';

const OrganizationDetails = ({ organizationId, readOnly=true }) => {
  const [ loading, setLoading ] = useState(true);
  const [ editingOrganizationDetails, setEditingOrganizationDetails ] = useState(false);
  const [ name, setName ] = useState('');
  const [ prevName, setPrevName ] = useState('');
  const [ nameErrorMsg, setNameErrorMsg ] = useState('');

  useEffect(() => {
    if (organizationId && organizationId !== '') {
      OrganizationApi.retrieve(organizationId)
      .then((response) => {
        const organization = response.data;
        setName(organization['name']);
        setLoading(false);
        return response;
      });
    }
  }, []);

  useEffect(() => {
    if (name !== '') {
      setNameErrorMsg('');
    } else {
      setNameErrorMsg(REQUIRED_FIELD_MESSAGE);
    }
  }, [name]);

  const restoreOrganizationDetails = () => {
    setName(prevName);
    setEditingOrganizationDetails(!editingOrganizationDetails);
  };

  const saveOrganizationDetails = async (e) => {
    e.preventDefault();

    if (editingOrganizationDetails) {
      const updatedFields = {};
      if (name !== prevName) {
        updatedFields['name'] = name;
      }
      // TODO: call the api to partially update the organization details
    }

    setPrevName(name);
    setEditingOrganizationDetails(!editingOrganizationDetails);
  };

  return (
    <Card elevation={0}>
      <CardHeader title='Organization Details'/>
      <CardContent>
        { loading 
          ?
          <Loading />
          :
          <Box
            component='form'
            autoComplete='off'
            sx={{ flexGrow: 1 }}
            className='m-2'
          >
            <Grid container>
              <Grid item xs={4} className='m-2'>
                <TextField
                  required={editingOrganizationDetails}
                  type='text'
                  label='Name'
                  variant='outlined'
                  size='small'
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  fullWidth
                  InputProps={{ readOnly: !editingOrganizationDetails }}
                  InputLabelProps={{ shrink: true }}
                  error={nameErrorMsg !== ''}
                  helperText={nameErrorMsg}
                />
              </Grid>
            </Grid>
            { !readOnly && 
              <Grid container>
                <Grid item className='m-2'>
                  <Button 
                    variant='contained'
                    disableElevation
                    onClick={saveOrganizationDetails}
                    disabled={
                      editingOrganizationDetails &&
                      (name === '')
                    }
                  >
                    { editingOrganizationDetails ? 'Save' : 'Edit' }
                  </Button>
                </Grid>
                { 
                  editingOrganizationDetails 
                  &&
                  <Grid item className='m-2'>
                    <Button
                      variant='contained'
                      color='error'
                      disableElevation
                      onClick={restoreOrganizationDetails}
                    >
                      Cancel
                    </Button>
                  </Grid>
                }
              </Grid>
            }
          </Box>
        }
      </CardContent>
    </Card>
  );
}

export default OrganizationDetails;