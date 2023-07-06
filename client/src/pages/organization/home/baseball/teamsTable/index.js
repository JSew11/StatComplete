import { useEffect, useState } from 'react';
import Table from '@mui/material/Table';
import TableHead from '@mui/material/TableHead';
import TableBody from '@mui/material/TableBody';

import OrganizationApi from 'src/api/organization';
import Loading from 'src/components/loading';
import StyledTableRow from 'src/components/styledTable/row';
import StyledTableCell from 'src/components/styledTable/cell';

const BaseballTeamsTable = ({ organizationId }) => {
  const [ loading, setLoading ] = useState(true);
  const [ teamRowData, setTeamRowData ] = useState([]);

  useEffect(() => {
    if (organizationId && organizationId !== '') {
      OrganizationApi.list_baseball_teams(organizationId)
      .then(
        (response) => {
          const rows = [];
          response.data.map((teamJson) => {
            rows.push({
              name: teamJson.name,
              location: teamJson.location
            })
          });
          setTeamRowData(rows);
          setLoading(false);
          return response;
        }
      );
    }
  }, []);

  return (
    <>
      {
        loading ?
          <Loading />
        :
          <Table stickyHeader size='small' className='mb-2'>
            <TableHead>
              <StyledTableRow>
                <StyledTableCell>Team</StyledTableCell>
                <StyledTableCell>Location</StyledTableCell>
              </StyledTableRow>
            </TableHead>
            <TableBody>
              { teamRowData.map((row) => (
                <StyledTableRow key={row.id}>
                  <StyledTableCell component='th' scope='row'>{row.name}</StyledTableCell>
                  <StyledTableCell>{row.location}</StyledTableCell>
                </StyledTableRow>
              ))}
            </TableBody>
          </Table>
      }
    </>
  );
}

export default BaseballTeamsTable;