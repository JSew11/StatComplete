import { useParams } from 'react-router-dom';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';

import OrganizationDetails from '../details';
import BaseballCompetitionsTable from 'src/components/baseball/competitionsTable';
import BaseballTeamsTable from 'src/components/baseball/teamsTable';

const OrganizationHome = () => {
  const { organizationId } = useParams();
  
  return (
    <Container>
      <Grid className='py-2'>
        <Grid item>
          <OrganizationDetails organizationId={organizationId} />
        </Grid>
      </Grid>
      <Grid className='py-2'>
        <Grid item>
          <Card elevation={0}>
            <CardHeader title='Baseball'/>
            <CardContent>
              <Grid className='py-1'>
                <BaseballCompetitionsTable organizationId={organizationId}/>
              </Grid>
              <Grid className='py-1'>
                <BaseballTeamsTable organizationId={organizationId}/>
              </Grid>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default OrganizationHome;