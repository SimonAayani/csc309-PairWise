import React, { Component } from "react";
import { Grid, Segment } from 'semantic-ui-react'
import Sidebar from './Sidebar.js'
import Notifications from './Notifications.js'
import './Dashboard.css'

class Dashboard extends Component {
    render() {
        return (
            <div className="App">
		        <Grid centered columns="two">
		          <Grid.Row centered columns="four">
		            <Grid.Column width={3} left floated>
		              <Segment id="side">
		              	<Sidebar />
		              </Segment>
		            </Grid.Column>
		            <Grid.Column width={8} right floated>
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

