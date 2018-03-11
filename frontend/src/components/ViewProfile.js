import React, { Component } from 'react'
import { Card, Image, Icon, Divider, Container, Button, Modal, Header, Grid } from 'semantic-ui-react'
import './ViewProfile.css'

class Profile extends Component {
  state = { open : false }

  show = dimmer => () => this.setState({ dimmer, open : true })
  close = () => this.setState({ open : false })

  render() {
    const { open, dimmer } = this.state

    return (
      <div className="fullProfile">
        <div className="modalHeight">
        <Modal dimmer={dimmer} open={open} onClose={this.close} closeIcon size='small'>
          <Modal.Header>
            <Grid columns={2} relaxed>
              <Grid.Column>
                <Header content={this.props.userInfo.name} subheader={this.props.userInfo.location} />
              </Grid.Column>
              <Divider vertical />
              <Grid.Column>
                <Button basic floated='right' color='teal'>Send Message</Button>
              </Grid.Column>
            </Grid>
          </Modal.Header>
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
          <Card fluid raised>
            <div className="matchPercentage">{this.props.userInfo.match}%</div>
            <Card.Header textAlign="left">
              <Image spaced="left" src={this.props.userInfo.picture} size='tiny' circular bordered floated="left"/>
              <div className="cardName">
                <Header>{this.props.userInfo.name}</Header>
              </div>
              <Card.Meta name="location">
                <Icon name='marker'/> {this.props.userInfo.location}
              </Card.Meta>
            </Card.Header>
            <Card.Description fluid>{this.props.userInfo.bio}</Card.Description>
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
