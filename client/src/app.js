import React from 'react';
import './App.css';
import { BrowserRouter } from 'react-router-dom';

import Routes from 'src/routes';

const App = () => {
  return (
    <BrowserRouter>
      <Routes />
    </BrowserRouter>
  );
}

export default App;
