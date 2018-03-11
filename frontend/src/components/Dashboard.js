import React, { Component } from "react";
import { Route, Link, Switch } from 'react-router-dom'

import { Grid, Segment } from 'semantic-ui-react'

import Sidebar from './Sidebar'
import Notifications from './Notifications'
import SearchResults from './SearchResults'
import NavBar from './NavBar';

import './Dashboard.css'

class Dashboard extends Component {
    render() {
        return (
            <div className="dashContainer">
		        <Grid centered columns="two">
		          <Grid.Row centered columns="four">
		            <Grid.Column width={4}>
		              <Segment id="sideContainer">
		              	<Sidebar />
		              </Segment>
		            </Grid.Column>
		            <Grid.Column width={1}></Grid.Column>
		            <Grid.Column width={8}>
		              <Segment padded id="contentContainer">
		              	<Switch>
		              		<Route exact path='/' component={Notifications} />
		              		<Route exact path='/dashboard' component={Notifications} />
		              		<Route path='/dashboard/searchResults/' component={SearchResults} />
		              	</Switch>
		              </Segment>
		            </Grid.Column>
		          </Grid.Row>
		        </Grid>
		    </div>
        )
    }

    
}

export default Dashboard;

