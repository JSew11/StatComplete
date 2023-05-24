import { Outlet } from 'react-router-dom';

import Header from 'src/components/layout/Header';

const Layout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
}

export default Layout;