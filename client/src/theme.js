import { createTheme } from '@mui/material/styles';

export const appTheme = createTheme({
  palette: {
    background: {
      default: '#eaebec',
      paper: '#ffffff'
    },
    primary: {
      light: '#7a98cc',
      main: '#29426c',
      dark: '#192841',
      contrastText: '#ffffff',
    },
    secondary: {
      light: '#9f7f39',
      main: '#885f08',
      dark: '#5f4205',
      contrastText: '#ffffff',
    },
  },
  components: {
    MuiButtonBase: {
      defaultProps: {
        disableRipple: true,
      },
    }
  }
});