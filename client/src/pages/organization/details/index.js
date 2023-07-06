import { useEffect, useState } from 'react';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';

import OrganizationApi from 'src/api/organization';
import Loading from 'src/common/loading';

const REQUIRED_FIELD_MESSAGE = 'This field is required.';

const OrganizationDetails = ({ organizationId }) => {
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
          </Box>
        }
      </CardContent>
    </Card>
  );
}

export default OrganizationDetails;