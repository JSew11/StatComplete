import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';

import OrganizationDetailsForm from '../detailsForm';
import BaseballCompetitionsTable from 'src/components/baseball/competitionsTable';
import BaseballTeamsTable from 'src/components/baseball/teamsTable';
import OrganizationApi from 'src/api/organization';
import Loading from 'src/components/loading';

const OrganizationHome = () => {
  const { organizationId } = useParams();
  
  const [ loading, setLoading ] = useState(true);
  const [ organization , setOrganization ] = useState({});

  useEffect(() => {
    if (organizationId && organizationId !== '') {
      OrganizationApi.retrieve(organizationId)
      .then((response) => {
        setOrganization(response.data);
        setLoading(false);
        return response;
      });
    }
  }, []);

  return (
    <Container>
      <Grid className='py-2'>
        <Grid item>
          <Card elevation={0}>
            <CardHeader title='Organization Details'/>
            <CardContent>
              { loading 
                ?
                <Loading />
                :
                <OrganizationDetailsForm organization={organization}/>
              }
            </CardContent>
          </Card>
        </Grid>
      </Grid>
      <Grid className='py-2'>
        <Grid item>
          <Card elevation={0}>
            <CardHeader title='Baseball'/>
            <CardContent>
              <BaseballCompetitionsTable organizationId={organizationId}/>
              <BaseballTeamsTable organizationId={organizationId}/>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default OrganizationHome;