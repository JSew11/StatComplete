import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';

import Layout from 'src/components/layout';
import Dashboard from 'src/pages/dashboard';
import Login from 'src/pages/user/auth/login';
import Register from 'src/pages/user/auth/register';
import UserProfile from 'src/pages/user/profile';
import OrganizationSearch from 'src/pages/organization/search';
import OrganizationLayout from './components/organization/layout';
import OrganizationHome from './pages/organization/home';
import Error404 from './pages/error404';

const Routes = () => (
  <Switch>
    <Route exact path='login/' Component={Login} />
    <Route exact path='register/' Component={Register} />
    <Route exact path='profile/' Component={UserProfile} />
    <Route Component={Layout}>
      <Route path='/' Component={Dashboard} />
      <Route path='organizations/' Component={OrganizationSearch} />
    </Route>
    <Route path='organizations/:organizationId/' Component={OrganizationLayout}>
      <Route path='' Component={OrganizationHome} />
    </Route>
    <Route path='*' Component={Error404} />
  </Switch>
);

export default Routes;