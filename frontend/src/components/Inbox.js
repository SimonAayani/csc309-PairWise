import React, { Component } from 'react';
import { Route, NavLink, BrowserRouter, withRouter } from "react-router-dom";
import Select from 'react-select';
//import './Inbox.css';
import { Button, Grid, Tab, Image, Icon, Label, Checkbox, Form, Modal, Dropdown, Input } from "semantic-ui-react";

import courseList from './data/courseList.js';
import { languages, frameworks, concepts } from './data/optionLists.js';

class Inbox extends Component {

  state = { modalOpen: false }

  handleOpen = () => this.setState({ modalOpen: true })

  handleClose = () => this.setState({ modalOpen: false })

  render () {  
     

    const panes = [
      { menuItem: 'Most Recent',
        pane: (
          <Tab.Pane key =  "1">
            <div>
              

            </div>
            
          </Tab.Pane>
      ) },

      { menuItem: 'Search Threads',
        pane: (
          <Tab.Pane key = "2">
            
          </Tab.Pane>
        ) },

      { menuItem: 'Group Threads',
        pane: (
          <Tab.Pane key = "3">
            
          </Tab.Pane>
        ) },

      
    ]

      

  if (this.props.isLoggedIn) {
            return(<NavLink to="/logout" onClick={this.props.handleLogout}>Log Out</NavLink>)
    }
    
      return(


        
      <div className="InboxComp">
      
        <h2 >
        <i class="circular inbox icon floated right"></i>
          My Inbox
        </h2>

          
      <Grid textAlign='center' style = {{marginTop: '25px'}}>
        <Grid.Column width={15}>

        <Tab menu={{ fluid: true, vertical: true, tabular: 'right'}} panes={panes}  renderActiveOnly={false}/>

        </Grid.Column>
      </Grid>
      </div>
    )    
    
  
  }

   
  
}

export default withRouter(Inbox);
