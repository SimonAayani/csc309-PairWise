import React from 'react'
import 'semantic-ui-css/semantic.min.css'
import { Card, Image, Icon } from 'semantic-ui-react'
/*import default_pic from './no-img.jpg';*/

const ProfileCard = () => (
  <Card>
    <Image src='https://chipinworld.com/assets1/images/about-image/no-image.jpg' /> {/* Need to fix*/}
    <Card.Content>
      <Card.Header>FirstName LastName</Card.Header>
      <Card.Meta>Location</Card.Meta>
      <Card.Description>This is the user's bio. Just adding a little text to make
      it longer for now.</Card.Description>
    </Card.Content>
    <Card.Content fullProfile>
      <a>
        <Icon name='fullProfile' />
        View Full Profile
      </a>
    </Card.Content>
  </Card>
)

export default ProfileCard
