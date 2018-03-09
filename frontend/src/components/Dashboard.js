import React, { Component } from 'react';

class Dashboard extends Component {
  render() {
    return (
      <div className="dashboard">
      <h1>This is the dashboard.</h1>
      <p>You should only see this when you're logged in.</p>
      </div>
    )
  }
}

export default Dashboard;
