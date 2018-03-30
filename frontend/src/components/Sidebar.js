import React, { Component } from 'react'
import { NavLink } from 'react-router-dom'

import { Accordion, Menu, Button, Segment, Label } from 'semantic-ui-react'

import './Sidebar.css'

export default class Sidebar extends Component {

  render() {
    const panels = [
      {
        title: {
            content: <Label color='blue' size="large">
                      Searches <i class=" right search icon"></i></Label>,
            key: 0
          },
        content: {
          content: (
            <div>
            <Segment className="sideOption" inverted color='teal'>
              <Button color='teal' name='newSearch'>
                <NavLink to="/dashboard/newsearch" className="sideLink">
                  New Search <i class=" right plus icon"></i>
                </NavLink>
              </Button>
            </Segment>
            </div>
          ),
          key: 0
        }
      }, {
        title: {
          content: <Label color='blue' size="large">
                      Groups <i class=" right users icon"></i></Label>,
          key: 1
        },
        content: {
          content: (
              <div>
              </div>
              ),
            key: 1
        }
      }
    ]

    return (
      /** Sidebar Component **/
      <Segment inverted vertical id="sidebar">
        <Menu.Item id="category-wrapper">
          <Accordion inverted styled defaultActiveIndex={[0]} panels={panels} exclusive={false} id="category" />
        </Menu.Item>
      </Segment>
    )
  }

}