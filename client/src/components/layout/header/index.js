import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

import Navbar from 'src/components/layout/navbar';
import UserDropdown from 'src/components/userDropdown';
import './index.css';

export default function Header() {
  const navigate = useNavigate();

  const { isLoggedIn } = useSelector(state => state.auth);
  
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container className='p-2 align-items-center'>
        <Grid item xs={8} onClick={() => {navigate('/');}} className='py-0 site-logo text-start'><h1>StatComplete</h1></Grid>
        <Grid item xs={4} className='m-0 p-0 text-end'><UserDropdown isLoggedIn={isLoggedIn} /></Grid>
      </Grid>
      <Grid>
        <Navbar />
      </Grid>
    </Box>
  );
}