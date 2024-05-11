import { CssBaseline } from "@mui/material";
import { Outlet } from "react-router-dom";

/**
 * This is a the default parent component, which is used for **all** Admin views.
 *
 * The individual routes are mounted into the `Outlet` component.
 */
export default function AdminLayout() {
    return (
        <div className="preflight flex flex-row">
            <CssBaseline />
            <Outlet />
        </div>
    );
}
