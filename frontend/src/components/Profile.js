import React, { Component } from "react";
import { Button, Grid, Tab, Image, Icon, Label, Checkbox, Form } from "semantic-ui-react";
import avatar from '../avatar.png'



export default class Profile extends Component{
	


	render() {


		const panes = [
  		{ menuItem: 'Profile', 
  			pane: (
  				<Tab.Pane key = "1">
    				<div>
    					<Button basic floated = "right" icon>
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

  		{ menuItem: 'Security', 
  			pane: (
  				<Tab.Pane key = "2">
            <Form>
              <Form.Field  inline>
                <label>Old Password:</label>
                <input placeholder='Old Password' />
              </Form.Field>
              <Form.Field  inline>
                <label>New Password:</label>
                <input placeholder='New Password' />
              </Form.Field>
              <Form.Field  inline>
                <label>Comfirm Password:</label>
                <input placeholder='Passowrd Again' />
              </Form.Field>
              <Button type='submit' basic color='blue'>Submit</Button>
            </Form>
  				</Tab.Pane>
  			) },

  		{ menuItem: 'Notifiction', 
  			pane: (
  				<Tab.Pane key = "3">
            <Form>
              <Form.Field  inline>
                <Checkbox toggle />
                <label>Pop up Notifiction:</label>
              </Form.Field>
              <Form.Field  inline>
                <Checkbox toggle />
                <label>Send Notifiction by E-mail:</label>
              </Form.Field>
            </Form>         
  				</Tab.Pane>
  			) },

  		{ menuItem: 'Social',
			pane: (
  				<Tab.Pane key = "4">
            <Form>
              <Form.Field  inline>
                <Checkbox toggle />
                <label>Active Search</label>
              </Form.Field>
            </Form>
  				</Tab.Pane>
  			) },
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
