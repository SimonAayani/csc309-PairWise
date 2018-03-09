import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
class Splash extends Component {

  render() {
    return (
      <div className="splash">
      <h1>This is the splash page.</h1>
      <p>You should only see this if you haven't logged in.</p>
      <button onClick={this.props.handleLogin}>Click to log in</button>
      </div>
    )
  }
}

export default withRouter(Splash);
