import { useEffect, useState } from 'react';
import {
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
} from '@mui/material';

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

  return (
    <div>
      { loading ?
          <Loading />
        :
          <Table stickyHeader size='small'>
            <TableHead>
              <TableRow>
                <TableCell>Competition Name</TableCell>
                <TableCell align='right'>Type</TableCell>
                <TableCell align='right'>Start Date</TableCell>
                <TableCell align='right'>End Date</TableCell>
                <TableCell align='right'>Status</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              { rowData.map((row) => (
                <TableRow key={row.id}>
                  <TableCell component='th' scope='row'>{row.name}</TableCell>
                  <TableCell align='right'>{row.type}</TableCell>
                  <TableCell align='right'>{row.startDate}</TableCell>
                  <TableCell align='right'>{row.endDate}</TableCell>
                  <TableCell align='right'>{row.status}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
      }
    </div>
  );
}

export default BaseballCompetitionsTable;