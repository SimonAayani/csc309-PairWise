import React, { Component } from 'react';
import { Button, Card, Image } from 'semantic-ui-react'
import SearchResultCard from './SearchResultCard'
import logo from '../logo.svg'

export default class SearchResults extends Component {

  render() {
    const results = [
      {
        userName: "Lisa",
        userMeta: "90% match",
        userDesc: "This is Lisa's description.",
        userPic: {logo}
      },
      {
        userName: "Harry",
        userMeta: "80% match",
        userDesc: "This is Harry's description.",
        userPic: {logo}
      },
      {
        userName: "Benny",
        userMeta: "75% match",
        userDesc: "This is Benny's description.",
        userPic: {logo}
      }
    ]



    return (
      <Card.Group>

        {results.map((result, i) => 
          <SearchResultCard key={i} {...result} />)}

      </Card.Group>
    )
  }
}