import React, { Component } from 'react';
import { Button, Card, Image } from 'semantic-ui-react'
import logo from '../logo.svg'

export default class SearchResultCard extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Card fluid>
        <Card.Content>
          <Image floated='right' size='mini' src={logo} />
          <Card.Header>
            {this.props.userName}
          </Card.Header>
          <Card.Meta>
            {this.props.userMeta}
          </Card.Meta>
          <Card.Description>
            {this.props.userDesc}
          </Card.Description>
        </Card.Content>
        <Card.Content extra>
          <div className='ui two buttons'>
            <Button basic color='teal'>View Profile</Button>
            <Button basic color='teal'>Send Message</Button>
          </div>
        </Card.Content>
      </Card>
    )
  }
}