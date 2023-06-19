import { useEffect, useState } from 'react';
import {
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
} from '@mui/material';
import { tableCellClasses } from '@mui/material/TableCell';
import { styled } from '@mui/material/styles';

import OrganizationApi from 'src/api/organization';
import { SEASON, TOURNAMENT, UNKNOWN } from 'src/utils/constants/competitionTypes';
import { COMPLETE, SCHEDULING, IN_PROGRESS, SCHEDULED } from 'src/utils/constants/competitionStatusTypes';
import Loading from 'src/components/loading';

const BaseballCompetitionsTable = ({ organizationId }) => {
  const [ loading, setLoading ] = useState(true);
  const [ rowData, setRowData ] = useState([]);

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
          setRowData(rows);
          setLoading(false);
          return response;
        }
      );
    }
  }, []);

  const StyledTableCell = styled(TableCell) (({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
      backgroundColor: theme.palette.primary.main,
      color: theme.palette.primary.contrastText,
      fontWeight: 'bold',
    },
    [`&.${tableCellClasses.body}`]: {
      fontSize: 14,
    },
  }));

  const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
    // hide last border
    '&:last-child td, &:last-child th': {
      border: 0,
    },
  }));

  return (
    <div>
      { loading ?
          <Loading />
        :
          <Table stickyHeader size='small'>
            <TableHead>
              <StyledTableRow>
                <StyledTableCell>Competition Name</StyledTableCell>
                <StyledTableCell align='right'>Type</StyledTableCell>
                <StyledTableCell align='right'>Start Date</StyledTableCell>
                <StyledTableCell align='right'>End Date</StyledTableCell>
                <StyledTableCell align='right'>Status</StyledTableCell>
              </StyledTableRow>
            </TableHead>
            <TableBody>
              { rowData.map((row) => (
                <StyledTableRow key={row.id}>
                  <StyledTableCell component='th' scope='row'>{row.name}</StyledTableCell>
                  <StyledTableCell align='right'>{row.type}</StyledTableCell>
                  <StyledTableCell align='right'>{row.startDate}</StyledTableCell>
                  <StyledTableCell align='right'>{row.endDate}</StyledTableCell>
                  <StyledTableCell align='right'>{row.status}</StyledTableCell>
                </StyledTableRow>
              ))}
            </TableBody>
          </Table>
      }
    </div>
  );
}

export default BaseballCompetitionsTable;