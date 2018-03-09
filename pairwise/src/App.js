import React from 'react'
import 'semantic-ui-css/semantic.min.css'
import { Card, Image, Icon, Divider, Container } from 'semantic-ui-react'
/*import default_pic from './no-img.jpg';*/
const default_pic = 'https://chipinworld.com/assets1/images/about-image/no-image.jpg'

const ProfileCard = () => (
  <Card raised>
  <Card.Content>
    <Container textAlign='center'>
    <Image src={default_pic} size='small' circular bordered/>
    </Container>
    <Divider hidden />
      <Card.Header textAlign='center'>FirstName LastName</Card.Header>
      <Card.Meta>
        <Container textAlign='center'> 
          <Icon name='marker'/> Location
        </Container>
      </Card.Meta>
      <Card.Description>This is the user's bio. Just adding a little text to make
      it longer for now.</Card.Description>
    </Card.Content>
    <Card.Content>
      <a>
        View Full Profile
      </a>
    </Card.Content>
  </Card>
)

export default ProfileCard
