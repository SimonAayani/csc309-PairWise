import React, { Component } from 'react'
import { Accordion, Menu, Icon, Button, Transition, Advertisement, Segment } from 'semantic-ui-react'
import './Sidebar.css'

export default class Sidebar extends Component {
  state = { activeIndex: 0 }

  handleClick = (e, titleProps) => {
    const { index } = titleProps
    const { activeIndex } = this.state
    const newIndex = activeIndex === index ? -1 : index

    this.setState({ activeIndex: newIndex })
  }

  render() {
    const { activeIndex } = this.state

    return (
      <Segment inverted vertical fixed id="sidebar">
        <Button color='teal' id="btn-dash" dashActive={true}>
          Dash
          <Icon name='exclamation' id="icon-notif" />
        </Button>
        <Menu.Item id="category-wrapper">
          <Accordion as={Menu} inverted styled vertical id="category">
            <Accordion.Title active={activeIndex === 0} index={0} onClick={this.handleClick}>
              <Icon name='dropdown' />
              Searches
            </Accordion.Title>
            <Accordion.Content active={activeIndex === 0}>
              <Segment inverted color='teal'>
                <Button color='teal' name='CSC309' dashActive={false}>
                  CSC309
                </Button>
              </Segment>
              <Segment inverted color='teal'>
                <Button color='teal' name='CSC369'>
                  CSC369
                </Button>
              </Segment>
              <Segment inverted color='teal'>
                <Button color='teal' name='newSearch'>
                  New Search
                </Button>
              </Segment>
            </Accordion.Content>

            <Accordion.Title active={activeIndex === 1} index={1} onClick={this.handleClick}>
              <Icon name='dropdown' />
              Groups
            </Accordion.Title>
            <Accordion.Content active={activeIndex === 1}>
              <Segment inverted color='teal'>
                <Button color='teal' name='grp-csc309'>
                  CSC309 Group
                </Button>
              </Segment>
              <Segment inverted color='teal'>
                <Button color='teal' name='grp-csc369'>
                  CSC369 Group
                </Button>
              </Segment>
            </Accordion.Content>
          </Accordion>
        </Menu.Item>
      </Segment>
    )
  }
}