import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

import UserDropdown from 'src/components/userDropdown';
import './index.css';
import OrganizationNavbar from '../navbar';
import OrganizationApi from 'src/api/organization';

export default function OrganizationHeader() {
  const {organizationId} = useParams();
  
  const navigate = useNavigate();

  const [ organizationName, setOrganizatioName ] = useState('');

  const { isLoggedIn } = useSelector(state => state.auth);

  useEffect(() => {
    OrganizationApi.retrieve(organizationId)
    .then(
      (response) => {
        if (response.data) {
          setOrganizatioName(response.data.name);
        }

        return response;
      }
    );
  }, [organizationId]);

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container className='p-2 align-items-center'>
        <Grid item xs={2} onClick={() => {navigate('/');}} className='small-logo col-1 text-start'><h2>SC</h2></Grid>
        <Grid item xs={8} className='text-center'><h1>{organizationName}</h1></Grid>
        <Grid item xs={2} className='col-1 text-end'><UserDropdown isLoggedIn={isLoggedIn} /></Grid>
      </Grid>
      <Grid>
        <OrganizationNavbar organizationId={organizationId}/>
      </Grid>
    </Box>
  );
}