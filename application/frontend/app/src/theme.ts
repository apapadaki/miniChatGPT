import { createTheme } from "@mui/material/styles";
import { red } from "@mui/material/colors";

// Create a theme instance.
const theme = createTheme({
  palette: {
    background: {
      default: "#343541",
      paper: "#202123",
    },
    text: {
      primary: "#ffffff",
    },
    primary: {
      main: "#343541",
    },
    secondary: {
      main: "#ffffff",
    },
    error: {
      main: red.A400,
    },
  },
});

export default theme;
