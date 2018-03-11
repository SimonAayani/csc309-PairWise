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
          bio: "This is Lisa's description. This is Lisa's description. This is Lisa's description. This is Lisa's description.",
          picture: "https://cdn4.iconfinder.com/data/icons/eldorado-user/40/user-512.png",
          skills: "C, Java, Python",
          courses: "CSC309, CSC369"
        }
      },
      {
        userInfo: {
          name: "Harry",
          match: "80",
          location: "Toronto",
          bio: "This is Harry's description. This is Harry's description. This is Harry's description. This is Harry's description.",
          picture: "https://cdn4.iconfinder.com/data/icons/eldorado-user/40/user-512.png",
          skills: "C, Java, Python",
          courses: "CSC309, CSC369"
        }
      },
      {
        userInfo: {
          name: "Benny",
          match: "70",
          location: "Downtown Toronto",
          bio: "This is Benny's description. This is Benny's description. This is Benny's description. This is Benny's description.",
          picture: "https://cdn4.iconfinder.com/data/icons/eldorado-user/40/user-512.png",
          skills: "C, Java, Python",
          courses: "CSC309, CSC369"
        }
      }
    ]



    return (
      <Card.Group children={results.map((result, i) => 
          <Profile key={i} {...result} />)} />
    )
  }
}