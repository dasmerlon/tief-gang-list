import { Outlet, Link } from "react-router-dom";
import Navigation from "../components/navigation";

export default function AdminLayout() {
  return (
    <div className="preflight flex flex-row">
      <Navigation />
      <div id="page">
        <Outlet />
      </div>
    </div>
  );
}
