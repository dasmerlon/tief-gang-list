//
// This module is responsible for initializing all API namespaces that're
// created via OpenApi-generator.
//
import { EntryEventApi, EventApi, GuestApi, RegistrationApi } from "./api/apis";
import { Configuration } from "./api/runtime";

// Create the default configuration for our backend server.
const apiConfiguration = new Configuration({ basePath: "" });

// Initialize all api namespaces with that configuration.
const eventApi = new EventApi(apiConfiguration);
const entryEventApi = new EntryEventApi(apiConfiguration);
const guestApi = new GuestApi(apiConfiguration);
const registrationApi = new RegistrationApi(apiConfiguration);

export { eventApi, entryEventApi, guestApi, registrationApi };
