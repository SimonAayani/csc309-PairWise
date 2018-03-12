import React, { Component } from 'react';
import { Button, Card, Image, Container, Divider, Icon } from 'semantic-ui-react'
import Profile from './ViewProfile'
import logo from '../logo.svg'

export default class SearchResultCard extends Component {
  render() {
    return (
       <div className="profileCard">
          <Card raised>
            <Card.Content>
              <Container textAlign='center' name='picture'>
                <Image src={this.props.userInfo.picture} size='small' circular bordered/>
              </Container>
              <Divider hidden />
              <Card.Header textAlign='center'>{this.props.userInfo.name}</Card.Header>
              <Card.Meta name="location">
                <Container textAlign='center'> 
                  <Icon name='marker'/> {this.props.userInfo.location}
                </Container>
              </Card.Meta>
              <Card.Description>{this.props.userInfo.bio}</Card.Description>
            </Card.Content>
            <Button size='medium' compact onClick={this.show(true)}>
              View Full Profile
            </Button>
          </Card>
        </div>
    )
  }
}