import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

const Error404 = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container className='p-2'>
        <Grid item xs={12}><h1 className='text-center'>404: This page could not be found</h1></Grid>
      </Grid>
    </Box>
  );
};

export default Error404;