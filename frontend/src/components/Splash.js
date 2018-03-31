import React, { Component } from "react";
import Layout from './Layout';
import './Splash.css';
import { Button } from 'semantic-ui-react'
import splash_pic from '../splash_1.png'

class Splash extends Component {
  render() {
    return (
        <Layout type="loggedOut">
      <div className="row">
        <div className="column left">
          <img className="logo" src={splash_pic} />
        </div>

        <div className="column right">
          <h1 className="title">PairWise</h1>
          <div>
            <p className="sub-text">PairWise is a match making web app that helps students find their perfect group partners!</p>
            <h2 className="subheader">Create a profile!</h2>
            <p2 className="text">Enhance your profile with your skills and qualifications. Choose between certain criteria that you are expecting in potential group partners. Add a profile picture!</p2>
            <h2 className="subheader">Search for group partners.</h2>
            <p2 className="text">Search through different courses for group partners. Enter search criteria to get closer matches.</p2>
            <h2 className="subheader">Form groups.</h2>
            <p2 className="text">Make groups with other students you find in your search. Send invites to students of interest.</p2>
          </div>
          
          <div className="button">
            <Button color='teal' size='huge'>Get Started</Button>
          </div>

        </div>
      </div>

  </Layout>
    )
  }
}

export default Splash;

