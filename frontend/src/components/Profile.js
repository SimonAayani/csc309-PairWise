import React, { Component } from "react";
import { Button, Grid, Tab, Image, Icon, Label, Checkbox, Form, Modal, Dropdown, Input, Divider } from "semantic-ui-react";
import avatar from '../avatar.png'
import axios from "axios"



export default class MyProfile extends Component{
  constructor (props) {
    super(props)
    this.state = {
      modalOpen: false,
      skills: [],
      bio: "",
      courses:[],
      location: 1,
      pic:"",
      first : true,
      email : '',
      student:1,
    }
    this.bioChange = this.bioChange.bind(this);
    this.skillsChange = this.skillsChange.bind(this);
    this.updateProfile = this.updateProfile.bind(this);
    this.courseChange = this.courseChange.bind(this);
    this.locationChange = this.locationChange.bind(this);
  }

  handleOpen = () => this.setState({ modalOpen: true })

  handleClose = () => this.setState({ modalOpen: false})

  //updateProfile =() => this.setState({ modalOpen: false,
    //                                 first: false})
  updateProfile(){
    this.setState({
      modalOpen: false,
      first: false
    })
    const profile = {
      student: 1,
      skills: this.state.skills,
      bio : this.state.bio,
      location : this.state.location,
      courses : this.state.courses,
      pic: null,
    }


    axios.post("http://165.227.40.205:8000/users/profile/new/", profile)
    .then(repsonse => {
      if (repsonse.stauts >= 200 && repsonse.stauts < 300){
        console.log("work")
      }
      else{
        console.log("wrong")
      }})
    .catch(error => {console.log(error)})
    }

    

  bioChange(e) {
    this.setState({bio: e.target.value});
  }

  locationChange(e){
    this.setState({location: e.target.value})
    console.log(this.state.location)
  }

  courseChange(e, data) {
    const course = data.value.map(v => v)
    this.setState({courses: course})
    console.log(this.state.courses)
  }

  skillsChange(e, data) {
    this.setState({skills: data.value})
    console.log(this.state.skills)
  }

	render() {



		const panes = [
  		{ menuItem: 'Profile',
  			pane: (
  				<Tab.Pane key =  "1">
    				<div>
              <Image src = {avatar} size = "small" centered/>
              <Divider hidden />
                <div>
                {this.state.first
                  ? <p>Please Update your Profile</p>
                  : <div>
                    <p>Name: {this.state.name}</p>
                    <p>E-mail: {this.state.email}</p>
                    <p>Course: {this.state.course}</p>
                    <p>Skills: {this.state.skills}</p>
                    <p>Bio: {this.state.bio}</p>
                    </div>}
                </div>
              <Divider hidden/>
    					<Modal open={this.state.modalOpen} onClose={this.handleClose} trigger={<Button onClick={this.handleOpen} basic = "right" icon>
                <Icon name = 'setting' />Update Profile</Button>} size='small'>
                <Modal.Header>Profile:</Modal.Header>
                <Modal.Content>
                  <Form>
                    <Form.Field inline>
                      <label>Course:</label>
                      <Dropdown placeholder='Course' multiple selection options={course} onChange={this.courseChange}/>
                    </Form.Field>
                    <Form.Field  inline>
                      <label>Skills:</label>
                      <Dropdown placeholder='Skills' multiple selection options={skills} onChange={this.skillsChange}/>
                    </Form.Field>
                    <Form.Field  inline>
                      <label>Location</label>
                      <input type= "int" onChange={this.locationChange}></input>
                    </Form.Field>
                    <Form.Field  inline>
                      <label>Bio:</label>
                      <textarea type= "text" onChange={this.bioChange}></textarea>
                    </Form.Field>

                  </Form>
                </Modal.Content>
                <Modal.Actions>
                  <Button basic color='blue' onClick={this.handleClose} >
                    Close
                  </Button>
                  <Button basic color='blue' onClick={this.updateProfile} >
                    Update
                  </Button>
                </Modal.Actions>
              </Modal>

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
                <input placeholder='Password Again' />
              </Form.Field>
              <Button type='submit' basic color='blue'>Submit</Button>
            </Form>
  				</Tab.Pane>
  			) },

  		{ menuItem: 'Notifications',
  			pane: (
  				<Tab.Pane key = "3">
            <Form>
              <Form.Field  inline>
                <Checkbox toggle />
                <label>Popup notifications:</label>
              </Form.Field>
              <Form.Field  inline>
                <Checkbox toggle />
                <label>Send notifications by E-mail:</label>
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
  		<Grid textAlign='center' style = {{marginTop: '100px'}}>
  			<Grid.Column width={10}>

				<Tab menu={{ fluid: true, vertical: true, tabular: 'right'}} panes={panes}  renderActiveOnly={false}/>

  			</Grid.Column>
  		</Grid>
  	)
	}
}


const course = [
  {text: 'csc104', value: 1 },
  {text: 'csc108', value: 2 },
  {text: 'csc148', value: 3 },
  {text: 'csc207', value: 4 },
  {text: 'csc209', value: 5 },
  {text: 'csc301', value: 6 },
  {text: 'csc309', value: 7 },
  {text: 'csc369', value: 8 },
  {text: 'csc373', value: 9 },
  {text: 'csc404', value: 10 },
  {text: 'csc411', value: 11 },
  {text: 'csc412', value: 12 },
]

const skills = [
  {text: 'Java', value : 1},
  {text: 'C', value : 2},
  {text: 'C++', value : 3},
  {text: 'Python', value : 4},
]

const gender= [
  { key: 'male', text: 'Male', value: 'male' },
  { key: 'female', text: 'Female', value: 'female' },
]
