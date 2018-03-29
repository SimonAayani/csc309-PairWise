import React, { Component } from 'react'
import { Card } from 'semantic-ui-react'
import Profile from './ViewProfile'

export default class SearchResults extends Component {

  render() {
    const results = [
    ]



    return (
      <Card.Group children={results.map((result, i) => 
          <Profile key={i} {...result} />)} />
    )
  }
}