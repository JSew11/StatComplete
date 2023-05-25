import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';

import Layout from 'src/components/layout';
import Dashboard from 'src/pages/dashboard';
import Login from 'src/pages/user/auth/login';
import Register from 'src/pages/user/auth/register';
import UserProfile from 'src/pages/user/profile';
import Organization from 'src/pages/organization';

const Routes = () => (
  <Switch>
    <Route exact path='login/' Component={Login} />
    <Route exact path='register/' Component={Register} />
    <Route exact path='profile/' Component={UserProfile} />
    <Route Component={Layout}>
      <Route path='/' Component={Dashboard} />
      <Route path='organization/' Component={Organization} />
    </Route>
    {/* TODO: make a 404 page here */}
  </Switch>
);

export default Routes;