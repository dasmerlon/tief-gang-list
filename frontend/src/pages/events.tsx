import { Event as ApiEvent } from "../api/models";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { eventApi } from "../apis";

function Events() {
  const [events, setEvents] = useState<ApiEvent[] | undefined>(undefined);

  // Fetch a list of events once, when loading the component.
  useEffect(() => {
    eventApi.getListEventListGet().then((events) => setEvents(events));
  }, []);

  return (
    <div>
      <h1>Events</h1>
      {events?.map((event, index) => {
        return (
          <li key={index}>
            {event.name}
            <Link to={"event/" + event.id}> Go to event</Link>{" "}
          </li>
        );
      })}
    </div>
  );
}

export default Events;
