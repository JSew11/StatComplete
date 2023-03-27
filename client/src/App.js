import React, { Component, Fragment } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container } from 'reactstrap';
import './App.css';
import Header from './components/common/Header';

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
      </Fragment>
    );
  }
}

export default App;
