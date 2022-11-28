function Root() {
  return (
    <>
      <div id="sidebar">
        <h1>Tief Gang List</h1>
        <nav>
          <ul>
            <li>
              <a href={`events/current`}>Current Event</a>
            </li>
            <li>
              <a href={`events`}>List of Events</a>
            </li>
          </ul>
        </nav>
      </div>
      <div id="page"></div>
    </>
  );
}

export default Root;
