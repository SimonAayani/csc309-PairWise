import React, { Component } from 'react'
import 'semantic-ui-css/semantic.min.css'
import { Card, Image, Icon, Divider, Container, Button, Modal, Header } from 'semantic-ui-react'
import './ViewProfile.css'

class Profile extends Component {
  state = { open : false }

  show = dimmer => () => this.setState({ dimmer, open : true})
  close = () => this.setState({ open : false})

  render() {
    const { open, dimmer } = this.state

    return (
      <div className="fullProfile">
        <div className="modalHeight">
        <Modal dimmer={dimmer} open={open} onClose={this.close} closeIcon size='small'>
          <Modal.Header>{this.props.userInfo.name}</Modal.Header>
          <Modal.Content image>
            <Image scrolling
              wrapped
              size='medium'
              circular
              src={this.props.userInfo.picture}
            />
            <Modal.Description>
              <Header>Bio</Header>{this.props.userInfo.bio}
              <Header>Skills</Header>{this.props.userInfo.skills}
              <Header>Courses</Header>{this.props.userInfo.courses}
            </Modal.Description>
          </Modal.Content>
        </Modal>
        </div>

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
    </div>
    )
  }
}

export default Profile
