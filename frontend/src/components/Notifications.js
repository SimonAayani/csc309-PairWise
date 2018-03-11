import React, { Component } from 'react';
import { Feed } from 'semantic-ui-react'
import logo from '../logo.svg'
import './Notifications.css';

class Notifications extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="feedPanel">
        <h1>While you were away...</h1>
        <Feed>
          <Feed.Event>
              <Feed.Label image={logo} />
              <Feed.Content>
                <Feed.Summary>
                    You have <a>2 new messages</a> in the <a>CSC369</a> group
                    <Feed.Date>1 Hour Ago</Feed.Date>
                </Feed.Summary>
              </Feed.Content>
          </Feed.Event>

          <Feed.Event>
              <Feed.Label image={logo} />
              <Feed.Content>
                <Feed.Summary>
                    <a>Harry</a> sent you a message regarding <a>CSC301</a>
                    <Feed.Date>3 days ago</Feed.Date>
                </Feed.Summary>
              </Feed.Content>
          </Feed.Event>

          <Feed.Event>
              <Feed.Label image={logo} />
              <Feed.Content>
                <Feed.Summary>
                    <a>Lisa</a> invited you to join their group for <a>CSC301</a>
                    <Feed.Date>4 days ago</Feed.Date>
                </Feed.Summary>
              </Feed.Content>
          </Feed.Event>
        </Feed>
      </div>
    );
  }
}

export default Notifications;