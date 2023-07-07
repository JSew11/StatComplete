import { useEffect, useState } from 'react';
import Table from '@mui/material/Table';
import TableHead from '@mui/material/TableHead';
import TableBody from '@mui/material/TableBody';

import OrganizationApi from 'src/api/organization';
import { SEASON, TOURNAMENT, UNKNOWN } from 'src/utils/constants/competitionTypes';
import { COMPLETE, SCHEDULING, IN_PROGRESS, SCHEDULED } from 'src/utils/constants/competitionStatusTypes';
import Loading from 'src/common/loading';
import StyledTableRow from 'src/common/styledTable/row';
import StyledTableCell from 'src/common/styledTable/cell';

const BaseballCompetitionsTable = ({ organizationId }) => {
  const [ loading, setLoading ] = useState(true);
  const [ competitionRowData, setCompetitionRowData ] = useState([]);

  const getCompetitionTypeString = (typeInt) => {
    switch (typeInt) {
      case 1:
        return SEASON;
      case 2:
        return TOURNAMENT;
      default:
        return UNKNOWN;
    }
  };

  const getCompetitionStatus = (startDate, endDate) => {
    const currentDate = new Date();
    if (!startDate || !endDate) {
      return SCHEDULING;
    }
    if (currentDate > endDate) {
      return COMPLETE;
    }
    if (currentDate > startDate) {
      return IN_PROGRESS;
    }
    return SCHEDULED;
  };

  useEffect(() => {
    if (organizationId && organizationId !== '') {
      OrganizationApi.list_baseball_competitions(organizationId)
      .then(
        (response) => {
          const rows = [];
          response.data.map((competitionJson) => {
            let competitionType = getCompetitionTypeString(competitionJson.type);
            const startDate = competitionJson.start_date ? new Date(competitionJson.start_date) : null;
            const endDate = competitionJson.end_date ? new Date(competitionJson.end_date) : null;
            let status = getCompetitionStatus(startDate, endDate);

            rows.push({
              id: competitionJson.id,
              name: competitionJson.name,
              type: competitionType,
              startDate: startDate ? startDate.toDateString() : null,
              endDate: endDate ? endDate.toDateString() : null,
              status: status,
            });
          });
          setCompetitionRowData(rows);
          setLoading(false);
          return response;
        }
      );
    }
  }, []);

  return (
    <Table stickyHeader size='small' className='mb-2'>
      <TableHead>
        <StyledTableRow>
          <StyledTableCell>Competition</StyledTableCell>
          <StyledTableCell align='right'>Type</StyledTableCell>
          <StyledTableCell align='right'>Start Date</StyledTableCell>
          <StyledTableCell align='right'>End Date</StyledTableCell>
          <StyledTableCell align='right'>Status</StyledTableCell>
        </StyledTableRow>
      </TableHead>
      <TableBody>
        { loading ?
            <StyledTableRow>
              <StyledTableCell colSpan={5}>
                <Loading />
              </StyledTableCell>
            </StyledTableRow>
          :
            competitionRowData.map((row) => (
              <StyledTableRow key={row.id}>
                <StyledTableCell component='th' scope='row'>{row.name}</StyledTableCell>
                <StyledTableCell align='right'>{row.type}</StyledTableCell>
                <StyledTableCell align='right'>{row.startDate}</StyledTableCell>
                <StyledTableCell align='right'>{row.endDate}</StyledTableCell>
                <StyledTableCell align='right'>{row.status}</StyledTableCell>
              </StyledTableRow>
            ))
        }
      </TableBody>
    </Table>
  );
}

export default BaseballCompetitionsTable;