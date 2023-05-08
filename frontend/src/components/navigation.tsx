import Box from "@mui/material/Box";
import BottomNavigation from "@mui/material/BottomNavigation";
import BottomNavigationAction from "@mui/material/BottomNavigationAction";
import RestoreIcon from "@mui/icons-material/Restore";
import FavoriteIcon from "@mui/icons-material/Favorite";
import LocationOnIcon from "@mui/icons-material/LocationOn";
import MenuIcon from "@mui/icons-material/Menu";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import { Outlet, Link } from "react-router-dom";

export default function Navigation() {
  const SideBar = () => {
    return (
      <AppBar className="hidden sm:flex">
        <Toolbar variant="dense">
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            className="mr-2"
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" color="inherit" component="div">
            Side Bar
          </Typography>
        </Toolbar>
      </AppBar>
    );
  };

  const BottomNav = () => {
    return (
      <BottomNavigation showLabels className="sm:hidden">
        <BottomNavigationAction label="Recents" icon={<RestoreIcon />} />
        <BottomNavigationAction label="Favorites" icon={<FavoriteIcon />} />
        <BottomNavigationAction label="Nearby" icon={<LocationOnIcon />} />
      </BottomNavigation>
    );
  };

  const links = (
    <>
      <Link to={`events/current`}>Current Event</Link>
      <Link to={`events`}>List of Events</Link>
    </>
  );

  return <SideBar />;
}
