import { createBrowserRouter } from "react-router-dom";
import AdminLayout from "./layout/admin_layout";
import ErrorPage from "./pages/error";
import Events from "./pages/events";
import Event from "./pages/event";

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
