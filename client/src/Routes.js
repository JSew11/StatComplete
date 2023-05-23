import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';

import Layout from 'src/pages/layout';
import Dashboard from 'src/pages/dashboard';
import Login from 'src/pages/user/auth/login';
import Register from 'src/pages/user/auth/register';
import UserProfile from 'src/pages/user/profile';

const Routes = () => (
  <Switch>
    <Route exact path='login/' Component={Login} />
    <Route exact path='register/' Component={Register} />
    <Route exact path='profile/' Component={UserProfile} />
    <Route Component={Layout}>
      <Route path='/' Component={Dashboard} />
      {/* TODO: make a 404 page here */}
    </Route>
  </Switch>
);

export default Routes;