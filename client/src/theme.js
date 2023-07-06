import { createTheme } from '@mui/material/styles';

const PRIMARY_COLOR_LIGHT = '#7a98cc';
const PRIMARY_COLOR_MAIN = '#29426c';
const PRIMARY_COLOR_DARK = '#192841';

const SECONDARY_COLOR_LIGHT = '#9f7f39'
const SECONDARY_COLOR_MAIN = '#885f08';
const SECONDARY_COLOR_DARK = '#5f4205';

const SITE_BACKGROUND_COLOR = '#eaebec';

const CARD_BORDER_COLOR = '#dbdcdd';
const CARD_HEADER_BACKGROUND_COLOR = '#f2f3f4';

export const appTheme = createTheme({
  palette: {
    background: {
      default: SITE_BACKGROUND_COLOR,
      paper: '#ffffff',
    },
    primary: {
      light: PRIMARY_COLOR_LIGHT,
      main: PRIMARY_COLOR_MAIN,
      dark: PRIMARY_COLOR_DARK,
      contrastText: '#ffffff',
    },
    secondary: {
      light: SECONDARY_COLOR_LIGHT,
      main: SECONDARY_COLOR_MAIN,
      dark: SECONDARY_COLOR_DARK,
      contrastText: '#ffffff',
    },
  },
  components: {
    MuiButtonBase: {
      defaultProps: {
        disableRipple: true,
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          border: 'solid 1px ' + CARD_BORDER_COLOR,
          borderRadius: '0',
        }
      }
    },
    MuiCardHeader: {
      styleOverrides: {
        root: {
          background: CARD_HEADER_BACKGROUND_COLOR,
          borderBottom: 'solid 1px ' + CARD_BORDER_COLOR,
        }
      }
    },
    MuiTable: {
      styleOverrides: {
        root: {
          border: 'solid 1px ' + CARD_BORDER_COLOR
        }
      }
    }
  }
});