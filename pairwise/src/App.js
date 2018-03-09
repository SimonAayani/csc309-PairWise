import React from 'react'
import 'semantic-ui-css/semantic.min.css'
import { Image, Icon, Divider, Container, Header } from 'semantic-ui-react'
const default_pic = 'https://chipinworld.com/assets1/images/about-image/no-image.jpg'

const OtherUserProfile = () => (
<Container>
      <Image src={default_pic} size='small' circular bordered centered/>
      <Divider hidden />
      <Container textAlign='center'>
        <Header name='user_name' as='h1' textAlign='center'>
          FirstName LastName
        </Header>
        <Icon name='marker'/> Location
      </Container>
      <Divider hidden />
    <p name='bio'>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    </p>
    <Header as='h2'>Skills</Header>
      {skills}
    <Header as='h2'>Courses Currently Taking</Header>
      {courses}
    <p name='courses'>
    </p>
  </Container>
)

var skillsList = ["SQL", "JavaScript", "C", "Python", "Java", "React", "Node.js", "C++"]
var skills = CreateSkillsText(skillsList)

var coursesList = ["CSC369", "CSC301", "CSC309"]
var courses = CreateCoursesText(coursesList)


function CreateSkillsText(skillsList) {
  return skillsList.join(", ")
}

function CreateCoursesText(coursesList) {
  return coursesList.join(", ")
}

export default OtherUserProfile