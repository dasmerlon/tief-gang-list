import { Event as ApiEvent } from "../api/models";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { eventApi } from "../apis";

function EventPage() {
  const [event, setEvent] = useState<ApiEvent | undefined>(undefined);
  const { eventId } = useParams();

  if (eventId) {
    useEffect(() => {
      eventApi
        .getEventEventEventIdGet({ eventId })
        .then((event) => setEvent(event));
    }, []);
  }

  return <h1>Looking at event: {event?.name} </h1>;
}

export default EventPage;
