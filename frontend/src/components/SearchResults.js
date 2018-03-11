import React, { Component } from 'react'
import { Card } from 'semantic-ui-react'
import Profile from './ViewProfile'

export default class SearchResults extends Component {

  render() {
    const results = [
      {
        userInfo: {
          name: "Lisa",
          match: "90",
          location: "Ajax",
          bio: "Hello everyone! I'm a third-year in computer science, and a commuter from out of town. Looking mostly for someone nice to work with, and you can count on me too to have a goof experience coding this term!",
          picture: "https://cdn4.iconfinder.com/data/icons/eldorado-user/40/user-512.png",
          skills: "C, Java, Python, Ruby, C++, Racket",
          email: "Lisa@mail.utoronto.ca",
          courses: "CSC309, CSC369"
        }
      },
      {
        userInfo: {
          name: "Harry",
          match: "80",
          location: "Toronto",
          bio: "I'm a hard worker and am aiming to get the best marks we can manage. Plenty of experience in large-scale projects, including full-stack development. Join me if you want to go overboard.",
          picture: "https://cdn4.iconfinder.com/data/icons/eldorado-user/40/user-512.png",
          skills: "C, Java, Python",
          email: "Harry@mail.utoronto.ca",
          courses: "CSC302, CSC469, CSC411, CSC488"
        }
      },
      {
        userInfo: {
          name: "Benny",
          match: "70",
          location: "Downtown Toronto",
          bio: "Specialist in database systems. Looking to create a web application, and looking for someone to help out in frontend.",
          picture: "https://cdn4.iconfinder.com/data/icons/eldorado-user/40/user-512.png",
          skills: "C, Java, Python, SQL, MySQL, PostgrSQL, Oracle, MongoDB",
          email: "Bennya@mail.utoronto.ca",
          courses: "CCSC301, CSC373, CSC343, CSC443"
        }
      }
    ]



    return (
      <Card.Group children={results.map((result, i) => 
          <Profile key={i} {...result} />)} />
    )
  }
}