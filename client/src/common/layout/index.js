import { Outlet } from 'react-router-dom';

import Header from 'src/common/layout/header';

const Layout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
}

export default Layout;