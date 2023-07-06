import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

const Dashboard = () => {
  const [ tempVar, setTempVar ] = useState('');

  const { isLoggedIn } = useSelector(state => state.auth);

  useEffect(() => {
    if (isLoggedIn) {
      // TODO: call API to get user-specific dashboard data
      setTempVar('Logged In');
    } else {
      // TODO: call API to get generic dashboard data
      setTempVar('Not Logged In');
    }
  }, [isLoggedIn]);

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container className='p-2'>
        <Grid item xs={12}><h2 className='text-center'>{tempVar}</h2></Grid>
      </Grid>
    </Box>
  );
}

export default Dashboard;