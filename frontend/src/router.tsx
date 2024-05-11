import { createBrowserRouter } from "react-router-dom";
import AdminLayout from "./layout/admin_layout";
import ErrorPage from "./pages/error";
import Events from "./pages/events";
import Event from "./pages/event";

/**
 * The router is responsible for mapping URLs to components.
 *
 * To create a new view that lives in its own URL, add that component
 * to the list below with its respective URL path.
 *
 * That component (element) is then mounted into the parent element
 * (e.g. AdminLayout), and replaces its `Outlet` component.
 */
const AppRouter = createBrowserRouter([
    {
        path: "/",
        element: <AdminLayout />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                element: <Events />,
            },
            {
                path: "/events",
                element: <Events />,
            },
            {
                path: "/event/new",
                element: <Event />,
            },
            {
                path: "/event/:eventId",
                element: <Event />,
            },
        ],
    },
]);

export default AppRouter;
