import React, { Component } from "react";
import { Button, Grid, Tab, Image } from "semantic-ui-react";
import avatar from '../avatar.png'



export default class Profile extends Component{
	


	render() {


		const panes = [
  		{ menuItem: 'Profile', 
  			pane: (
  				<Tab.Pane key = "1">
  				<Image src = {avatar} size = "small" />
      			</Tab.Pane>

  		) },
  		{ menuItem: 'Security', pane: { key: 'tab1', content: 'This is massive tab', size: 'massive' } },
  		{ menuItem: 'Notifiction', pane: { key: 'tab1', content: 'This is massive tab', size: 'massive' } },
  		{ menuItem: 'Social', pane: { key: 'tab1', content: 'This is massive tab', size: 'massive' } },
		]

    	return (
    		<Grid textAlign='center'>
    			<Grid.Column width={10}>
    			
  				<Tab menu={{ fluid: true, vertical: true, tabular: 'right'}} panes={panes} renderActiveOnly={false}/>

    			</Grid.Column>
    		</Grid>
    	)
  	}

}
