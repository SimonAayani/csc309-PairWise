import React, { Component } from "react";
import { withRouter } from "react-router-dom";

class Login extends Component {
  constructor(props) {
    super(props);

    this.redirectHome = this.redirectHome.bind(this);
  }

  redirectHome() {
    this.props.history.push("/");
  }

  render() {
    const handler = (e) => {
      this.props.handleLogin(e);
      this.redirectHome();
    }

    return (
      <div className="login">
        <h2>Login</h2>
        <button onClick={handler}>Log In</button>
      </div>
    )
  }
}

export default withRouter(Login);
