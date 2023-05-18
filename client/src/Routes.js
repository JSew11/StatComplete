import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';

import Layout from './pages/layout';
import Dashboard from './pages/dashboard';
import Login from './pages/login';
import Register from './pages/register';

const Routes = () => (
  <Switch>
    <Route Component={Layout}>
      <Route path='/' Component={Dashboard} />
    </Route>
    <Route path='login/' Component={Login} />
    <Route path='register/' Component={Register} />
  </Switch>
);

export default Routes;