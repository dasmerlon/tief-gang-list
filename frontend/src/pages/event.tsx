import { Event as ApiEvent } from "../api/models";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { eventApi } from "../apis";

function EventPage() {
    const [event, setEvent] = useState<ApiEvent | undefined>(undefined);
    const { eventId } = useParams();

    useEffect(() => {
        if (eventId) {
            eventApi
                .getEventApiEventEventIdGet({ eventId })
                .then((event) => setEvent(event));
        }
    }, [eventId]);

    return <h1>Looking at event: {event?.name} </h1>;
}

export default EventPage;
