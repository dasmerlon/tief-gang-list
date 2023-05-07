import { Event as ApiEvent } from "../api/models";
import { useEffect, useState } from "react";
import { eventApi } from "../apis";
import Button from "@mui/material/Button";

function Events() {
  const [events, setEvents] = useState<ApiEvent[] | undefined>(undefined);

  // Fetch a list of events once, when loading the component.
  useEffect(() => {
    eventApi.getListApiEventListGet().then((events) => setEvents(events));
  }, []);

  return (
    <div>
      <h1>Events</h1>
      {events?.map((event, index) => {
        return (
          <li className="" key={index}>
            {event.name}
            <Button variant="contained" href={"event/" + event.id}>
              Go to event
            </Button>
          </li>
        );
      })}
    </div>
  );
}

export default Events;
