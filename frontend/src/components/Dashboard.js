import React, { Component } from "react";
import { Route, Switch } from 'react-router-dom'

import { Grid, Segment } from 'semantic-ui-react'

import Sidebar from './Sidebar'
import SearchForm from './SearchForm'
import SearchResults from './SearchResults'
import Notifications from './Notifications'

import './Dashboard.css'

class Dashboard extends Component {
    render() {
        return (
            <div className="dashContainer">
		        <div id="sideContainer">
		        	<Sidebar />
		        </div>
		        <div id="contentContainer">
		        	<Switch>
		              	<Route exact path='/' component={Notifications} />	
	              		<Route exact path='/dashboard' component={Notifications} />
	              		<Route path='/dashboard/newsearch' component={SearchForm} />
	              		<Route path='/dashboard/searchresults/' component={SearchResults} />
	              	</Switch>
		        </div>
		    </div>
        )
    }

    
}

export default Dashboard;

