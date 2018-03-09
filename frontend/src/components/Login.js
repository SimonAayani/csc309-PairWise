import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import Dashboard from './Dashboard';

class Login extends Component {
  constructor(props) {
    super(props);

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    return <Redirect to="/dashboard" component={Dashboard} />
  }
  render() {
    return(
      <button onClick={this.handleClick}>Log In</button>
    )
  }
}

export default Login;
