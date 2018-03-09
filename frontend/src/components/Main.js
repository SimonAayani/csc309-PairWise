import React, { Component } from "react";
import { Route, NavLink, BrowserRouter } from "react-router-dom";

import Dashboard from './Dashboard';
import Login from './Login';
import Splash from './Splash';

class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {isLoggedIn: false};

    this.handleLogin = this.handleLogin.bind(this);
  }

  handleLogin(e) {
    e.preventDefault();
    this.setState({
      isLoggedIn: true
    });
    console.log("handle login called");
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    return (
      <BrowserRouter>
        <div className="main">
          <div className="header">
          <h1>PairWise</h1>
          <ul>
            <li><NavLink exact to="/">Home</NavLink></li>
            <li><NavLink to="/login">Login</NavLink></li>
          </ul>
        </div>
          <div className="content">
            <Route exact path="/" render={() => isLoggedIn ? <Dashboard /> : <Splash />} />
            <Route path="/login" render={() => <Login handleLogin={this.handleLogin} />} />
           <Route path="/splash" component={Splash}/>
          </div>

        </div>
      </BrowserRouter>
    )
  }
}

export default Main;
