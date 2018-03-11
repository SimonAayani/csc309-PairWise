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
              <Button color='teal' name='CSC309' onClick={this.handleClick}>
                <NavLink to="/dashboard/searchresults/csc309" className="sideLink">CSC309</NavLink>
              </Button>
            </Segment>

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
                <Segment className="sideOption" inverted color='teal'>
                    <Button color='teal' name='grp-csc309'>
                      CSC309 Group
                    </Button>
                  </Segment>
                </div>
              ),
            key: 1
        }
      }
    ]

    return (
      // Side Bar
      <Segment inverted vertical id="sidebar">
        <Button color='teal' id="btn-dash">
          <NavLink to="/dashboard" className="sideLink">Notifications &nbsp;&nbsp;
          {/*<Label circular color="blue" id="icon-notif">3</Label>*/}
          <i class=" right bell icon"></i></NavLink>
        </Button>
        <Menu.Item id="category-wrapper">
          <Accordion inverted styled defaultActiveIndex={[0]} panels={panels} exclusive={false} id="category" />
        </Menu.Item>
      </Segment>
    )
  }

}