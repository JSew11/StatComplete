import { Outlet } from 'react-router-dom';

import OrganizationHeader from './header';

const OrganizationLayout = () => {
  return (
    <>
      <OrganizationHeader />
      <Outlet />
    </>
  );
}

export default OrganizationLayout;