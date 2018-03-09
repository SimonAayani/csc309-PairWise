import React, { Component } from "react";

class Login extends Component {
    render() {
        return (
            <div className="login">
            <h2>Login</h2>
            <button onClick={this.props.handleLogin}>Log In</button>
            </div>
        )
    }
}

export default Login;
