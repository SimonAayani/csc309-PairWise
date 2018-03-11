import React, { Component } from "react";
import { Button, Grid, Tab, Image, Icon } from "semantic-ui-react";
import avatar from '../avatar.png'



export default class Profile extends Component{
	


	render() {


		const panes = [
  		{ menuItem: 'Profile', 
  			pane: (
  				<Tab.Pane key = "1">
  				<div>
  					<Button floated = "right" icon>
  						<Icon name = 'setting' />
  					</Button>
  				</div>
  				<Image src = {avatar} size = "small" centered/>
  				<div>
  					<p></p>
  					<p>Name: Parry</p>
  					<p>Birthday: 1996-05-08</p>
            		<p>Gender: Male</p>
            		<p>E-mail: parry@hotmail.com</p>
            		<p>Skill: Java</p>
  				</div>
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
