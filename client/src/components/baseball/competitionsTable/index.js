import { useEffect, useState } from 'react';
import {
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
} from '@mui/material';

import OrganizationApi from 'src/api/organization';

const BaseballCompetitionsTable = ({ organizationId }) => {
  const [ rowData, setRowData ] = useState([]);

  const getCompetitionTypeString = (typeInt) => {
    switch (typeInt) {
      case 1:
        return 'Season';
      case 2:
        return 'Tournament';
      default:
        return 'Unknown';
    }
  };

  const getCompetitionStatus = (startDate, endDate) => {
    const currentDate = new Date();
    if (!startDate || !endDate) {
      return 'Scheduling';
    }
    if (currentDate > endDate) {
      return 'Complete';
    }
    if (currentDate > startDate) {
      return 'In Progress';
    }
    return 'Scheduled';
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
          return response;
        }
      );
    }
  }, []);

  return (
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
  );
}

export default BaseballCompetitionsTable;