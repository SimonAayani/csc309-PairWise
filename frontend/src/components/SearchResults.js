import React, { Component } from 'react';
import { Button, Card, Image } from 'semantic-ui-react'
import logo from '../logo.svg'

export default class SearchResults extends Component {

  render() {
    return (
      <Card.Group>
        <Card fluid>
          <Card.Content>
            <Image floated='right' size='mini' src={logo} />
            <Card.Header>
              Steve Sanders
            </Card.Header>
            <Card.Meta>
              Friends of Elliot
            </Card.Meta>
            <Card.Description>
              Steve wants to add you to the group <strong>best friends</strong>
            </Card.Description>
          </Card.Content>
          <Card.Content extra>
            <div className='ui two buttons'>
              <Button basic color='green'>View Profile</Button>
              <Button basic color='green'>Send Message</Button>
            </div>
          </Card.Content>
        </Card>

        <Card fluid>
          <Card.Content>
            <Image floated='right' size='mini' src={logo} />
            <Card.Header>
              Molly Thomas
            </Card.Header>
            <Card.Meta>
              New User
            </Card.Meta>
            <Card.Description>
              Molly wants to add you to the group <strong>musicians</strong>
            </Card.Description>
          </Card.Content>
          <Card.Content extra>
            <div className='ui two buttons'>
              <Button basic color='green'>Approve</Button>
              <Button basic color='red'>Decline</Button>
            </div>
          </Card.Content>
        </Card>

        <Card fluid>
          <Card.Content>
            <Image floated='right' size='mini' src={logo} />
            <Card.Header>
              Jenny Lawrence
            </Card.Header>
            <Card.Meta>
              New User
            </Card.Meta>
            <Card.Description>
              Jenny requested permission to view your contact details
            </Card.Description>
          </Card.Content>
          <Card.Content extra>
            <div className='ui two buttons'>
              <Button basic color='green'>Approve</Button>
              <Button basic color='red'>Decline</Button>
            </div>
          </Card.Content>
        </Card>
      </Card.Group>
    )
  }
}