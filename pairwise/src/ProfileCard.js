import React, { Component } from 'react'
import 'semantic-ui-css/semantic.min.css'
import { Card, Image, Icon, Divider, Container, Button } from 'semantic-ui-react'
import User from "./User";

/*
var bio = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."
var name = "FirstName LastName"
var location = "Toronto"
const default_pic = 'https://chipinworld.com/assets1/images/about-image/no-image.jpg'*/

class ProfileCard extends Component {
  render() {
    return (
      <div className = "profileCard">
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
          <Button size='medium' compact>
            View Full Profile
          </Button>
        </Card>
    </div>
    )
  }
}

export default ProfileCard
