import React, { Component } from 'react';
import { Grid, Image, Feed, Icon } from 'semantic-ui-react'
import logo from '../logo.svg'
import './Notifications.css';

class Notifications extends Component {
  render() {
  	return (
  		<Feed display={this.state}>
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
          				<a>Lisa</a> invited you to join his group for <a>CSC301</a>
          				<Feed.Date>4 days ago</Feed.Date>
        			</Feed.Summary>
      			</Feed.Content>
    		</Feed.Event>
  		</Feed>
  	);
  }
}

export default Notifications;