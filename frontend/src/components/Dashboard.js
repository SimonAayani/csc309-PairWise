import React, { Component } from "react";
import { Grid, Segment } from 'semantic-ui-react'
import Sidebar from './Sidebar.js'
import Notifications from './Notifications.js'
import './Dashboard.css'
import NavBar from './NavBar.js';

class Dashboard extends Component {
    render() {
        return (
            <div className="App">

		        <Grid centered columns="two">
		          <Grid.Row centered columns="four">
		            <Grid.Column width={4} left floated>
		            
		              <Segment id="side">
		              	<Sidebar />
		              </Segment>
		            </Grid.Column>
		            <Grid.Column width={1}></Grid.Column>
		            <Grid.Column width={8} left floated>
		              <Segment padded id="contents">
		              	<Notifications />
		              </Segment>
		            </Grid.Column>
		          </Grid.Row>
		        </Grid>
		    </div>
        )
    }

    
}

export default Dashboard;

