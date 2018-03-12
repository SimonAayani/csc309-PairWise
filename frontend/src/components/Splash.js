import React, { Component } from "react";
import './Splash.css';

class Splash extends Component {
  render() {
    return (
      <div className="splash">
        <h1 className="display-5">PairWise</h1>

        <p1 className="lead" id="myP">PairWise is a match making web app that helps students find their perfect group partners! </p1>

        <div className="splash-inner">
          <h2>Create a profile!</h2>
          <p2>Enhance your profile with your skills and qualifications. Choose between certain criteria that you are expecting in potential group partners. Add a profile picture!</p2>
          <h2 className="c">Search for group partners.</h2>
          <p2>Search through different courses for group partners. Enter search criteria to get closer matches.</p2>
          <h2>Form groups.</h2>
          <p2>Make groups with other students you find in your search. Send invites to students of interest.</p2>
        </div>

      </div>
    )
  }
}

export default Splash;

