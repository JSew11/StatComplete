import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

const OrganizationSearch = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container className='p-2'>
        <Grid item xs={12}><h2 className='text-center'>Organization Search</h2></Grid>
      </Grid>
    </Box>
  );
}

export default OrganizationSearch;