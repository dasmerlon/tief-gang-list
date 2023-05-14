import { CssBaseline } from "@mui/material";
import { Outlet } from "react-router-dom";
import Navigation from "../components/navigation";

export default function AdminLayout() {
  return (
    <div className="preflight flex flex-row">
      <CssBaseline />
      <Navigation />
      <Outlet />
    </div>
  );
}
