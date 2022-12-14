import { BrowserRouter, Routes, Route } from "react-router-dom";

import Root from "./layout/root";
import ErrorPage from "./pages/error";
import Event from "./pages/event";
import Events from "./pages/events";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Root />} errorElement={<ErrorPage />}>
          <Route path="/" element={<Events />} />
          <Route path="/event/:eventId" element={<Event />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
