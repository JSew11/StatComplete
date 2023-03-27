import React, { Component, Fragment } from 'react';
import './App.css';
import Header from './components/common/Header';
import Navbar from './components/common/Navbar';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      'user_id': null,
      'user_token': null
    };
  }

  render() {
    return (
      <Fragment>
        <Header />
        <Navbar />
      </Fragment>
    );
  }
}

export default App;
