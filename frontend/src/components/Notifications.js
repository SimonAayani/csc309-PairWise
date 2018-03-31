import React, { Component } from 'react';
import Layout from './Layout';
import { List, Image } from 'semantic-ui-react'
import avatar from '../avatar.png'
import './Notifications.css';

class Notifications extends Component {

  render() {
    const items = [{
      image: {
        src: avatar,
        className: 'avatar'
      },
      header: 'Lisa',
      description: 'invited you to join their group for CSC309'
    }, {
      image: {
        src: avatar,
        className: 'avatar'
      },
      header: 'Harry',
      description: 'sent you a message regarding CSC369'
    }]

    return (
            <Layout type="loggedIn">
      <div>
        <div id="awayMsg"> While you were away... </div>
        
        <div className="feedPanel">
          <List relaxed='very' divided='true' items={items} />
        </div>
      </div>
            </Layout>
    );
  }
}

export default Notifications;
