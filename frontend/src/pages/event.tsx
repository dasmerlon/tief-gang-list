import { Event as ApiEvent } from "../api/models";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { EventApi } from "../api/apis/EventApi";
import { Configuration } from "../api/runtime";

function EventPage() {
  const [event, setEvent] = useState<ApiEvent | undefined>(undefined);
  const { eventId } = useParams();

  if (eventId) {
    useEffect(() => {
      const config = new Configuration({ basePath: "http://localhost:8000" });
      const api = new EventApi(config);
      api.getEventEventEventIdGet({ eventId }).then((event) => setEvent(event));
    }, []);
  }

  return <h1>Looking at event: {event?.name} </h1>;
}

export default EventPage;
