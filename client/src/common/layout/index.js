import { Outlet } from 'react-router-dom';

import Header from 'src/components/layout/header';

const Layout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
}

export default Layout;