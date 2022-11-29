import { Event as ApiEvent } from "../api/models";
import { useEffect, useState } from "react";
import { EventApi } from "../api/apis/EventApi";
import { Configuration } from "../api/runtime";
import { Link } from "react-router-dom";

function Events() {
  const [events, setEvents] = useState<ApiEvent[] | undefined>(undefined);

  // Fetch a list of events once, when loading the component.
  useEffect(() => {
    const config = new Configuration({ basePath: "http://localhost:8000" });
    const api = new EventApi(config);
    api.getListEventListGet().then((events) => setEvents(events));
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
