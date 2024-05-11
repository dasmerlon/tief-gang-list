import { Event as ApiEvent } from "../api/models";
import { useEffect, useState } from "react";
import { eventApi } from "../apis";
import {
    Button,
    Paper,
    TableContainer,
    Table,
    TableRow,
    TableCell,
    TableHead,
    TableBody,
} from "@mui/material";
import { format_date } from "../i18n";
import { Link } from "react-router-dom";
import PageLayout from "../layout/page_layout";

function Events() {
    const [events, setEvents] = useState<ApiEvent[] | undefined>(undefined);

    // Fetch a list of events once, when loading the component.
    useEffect(() => {
        eventApi.getListApiEventListGet().then((events) => setEvents(events));
    }, []);

    return (
        <PageLayout title="Events">
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
                                        <Button variant="contained">
                                            <Link to={"event/" + event.id}>Edit</Link>
                                        </Button>
                                    </TableCell>
                                </TableRow>
                            );
                        })}
                    </TableBody>
                </Table>
            </TableContainer>
        </PageLayout>
    );
}

export default Events;
