import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';

import Layout from './pages/layout';
import Dashboard from './pages/dashboard';
import Login from './pages/login';
import Register from './pages/register';

const Routes = () => (
  <Switch>
    <Route exact path='login/' Component={Login} />
    <Route exact path='register/' Component={Register} />
    <Route Component={Layout}>
      <Route path='/' Component={Dashboard} />
      {/* TODO: make a 404 page here */}
    </Route>
  </Switch>
);

export default Routes;