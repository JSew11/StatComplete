import { useState } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';

const OrganizationDetailsForm = ({ organization }) => {
  const [ name, setName ] = useState(organization.name ?? '');

  return (
    <Box
      component='form'
      autoComplete='off'
      sx={{ flexGrow: 1 }}
      className='m-2'
    >
      <Grid container>
        <Grid item xs={4}>
          <TextField
            type='text'
            label='Name'
            variant='outlined'
            size='small'
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </Grid>
      </Grid>
    </Box>
  );
}

export default OrganizationDetailsForm;