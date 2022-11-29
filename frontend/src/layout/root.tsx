import { Outlet, Link } from "react-router-dom";

function Root() {
  return (
    <>
      <div id="sidebar">
        <h1>Tief Gang List</h1>
        <nav>
          <ul>
            <li>
              <Link to={`events/current`}>Current Event</Link>
            </li>
            <li>
              <Link to={`events`}>List of Events</Link>
            </li>
          </ul>
        </nav>
      </div>
      <div id="page">
        <Outlet />
      </div>
    </>
  );
}

export default Root;
