import CircularProgress from '@mui/material/CircularProgress';
import Grid from '@mui/material/Grid';

export default function Loading() {
  return (
    <>
      <Grid item className='p-2 align-items-center'>
        <div className='text-center'><CircularProgress /></div>
      </Grid>
      <Grid item className='p-2 align-items-center'>
        <div className='text-center'><h4 className='loading-text'>Loading</h4></div>
      </Grid>
    </>
  );
}