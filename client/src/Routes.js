import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';

import Layout from 'src/pages/layout';
import Dashboard from 'src/pages/dashboard';
import Login from 'src/pages/auth/login';
import Register from 'src/pages/auth/register';

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