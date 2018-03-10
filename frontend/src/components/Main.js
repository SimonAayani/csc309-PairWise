import React, { Component } from "react";
import { Route, NavLink, BrowserRouter } from "react-router-dom";

import Dashboard from './Dashboard';
import Login from './Login';
import Splash from './Splash';

class Main extends Component {
  constructor(props) {
    super(props);

    // for now, we'll model user authentication with a boolean state variable
    this.state = {isLoggedIn: false};

    // bindings
    this.handleLogin = this.handleLogin.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
  }

  // functions for toggling Login/Logout
  handleLogin(e) {
    e.preventDefault();
    this.setState({isLoggedIn: true});
  }

  handleLogout(e) {
    e.preventDefault();
    this.setState({isLoggedIn: false});
  }

  render() {
    return (
      <BrowserRouter>
        <div className="main">
          <div className="header">
            <h1>PairWise</h1>
            <ul>
              <li><NavLink exact to="/">Home</NavLink></li>
              <li><LoginLink
                    isLoggedIn={this.state.isLoggedIn}
                    handleLogin={this.handleLogin}
                    handleLogout={this.handleLogout}
                  /></li>
            </ul>
          </div>
          <div className="content">
            <Route exact path="/" render={() => this.state.isLoggedIn ? <Dashboard /> : <Splash />} />
            <Route path="/login" render={() =>
                <Login handleLogin={this.handleLogin} />
            } />
          <Route path="/splash" component={Splash}/>
          <Route path="/dashboard" component={Dashboard}/>
          <Route path="/logout" component={Splash} />
        </div>

      </div>
    </BrowserRouter>
    )
  }
}

class LoginLink extends Component {
  render() {
    if (this.props.isLoggedIn) {
      return(<NavLink to="/logout" onClick={this.props.handleLogout}>Log Out</NavLink>)
    } else {
      return(<NavLink to="/login">Log In</NavLink>)
    }
  }
}


export default Main;
