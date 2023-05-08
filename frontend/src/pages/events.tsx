import { Event as ApiEvent } from "../api/models";
import { useEffect, useState } from "react";
import { eventApi } from "../apis";
import Button from "@mui/material/Button";
import { Paper } from "@mui/material/Paper";
import TableContainer from "@mui/material/TableContainer";
import Table from "@mui/material/Table";
import TableRow from "@mui/material/TableRow";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableBody from "@mui/material/TableBody";
import { format_date } from "../i18n";

function Events() {
  const [events, setEvents] = useState<ApiEvent[] | undefined>(undefined);

  // Fetch a list of events once, when loading the component.
  useEffect(() => {
    eventApi.getListApiEventListGet().then((events) => setEvents(events));
  }, []);

  return (
    <>
      <h1>Events</h1>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }}>
          <TableHead>
            <TableRow>
              <TableCell>Event Name</TableCell>
              <TableCell align="right">Date</TableCell>
              <TableCell align="right">Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {events?.map((event, index) => {
              return (
                <TableRow
                  key={index}
                  sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {event.name}
                  </TableCell>
                  <TableCell align="right">{format_date(event.date)}</TableCell>
                  <TableCell align="right">
                    <Button variant="contained" href={"event/" + event.id}>
                      Edit
                    </Button>
                  </TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
}

export default Events;
