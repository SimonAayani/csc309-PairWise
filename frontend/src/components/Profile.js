import React, { Component } from "react";
import { Button, Grid, Tab, Image, Icon, Label, Checkbox, Form, Modal, Dropdown, Input, Divider } from "semantic-ui-react";
import avatar from '../avatar.png'



export default class MyProfile extends Component{
  constructor (props) {
    super(props)
    this.state = {
      modalOpen: false,
      skills: [],
      bio: "",
      course:[],
      location: 1,
      pic:"",
      first : true,
      email : '',
    }
    this.firstnameChange = this.firstnameChange.bind(this);
    this.bioChange = this.bioChange.bind(this);
    this.emailChange = this.emailChange.bind(this);
    this.skillsChange = this.skillsChange.bind(this);

  }

  handleOpen = () => this.setState({ modalOpen: true })

  handleClose = () => this.setState({ modalOpen: false})

  //updateProfile =() => this.setState({ modalOpen: false,
    //                                 first: false})
  updateProfile(){
    this.setState({ modalOpen: false,
                    first: false})
    const profile = {
      skills: this.state.skill,
      bio : this.state.bio
      location : this.state.location,
      course : this.state.course
    }
    axios.post("http://165.227.40.205:8000/users/profile/", profile)
    .then(repsonse => {
      if (repsonse.stauts >= 200 && repsonse.stauts < 300){
        console.log("work")
      }
      else{
        console.log("wrong")
      }})
    .catch(error => {console.log(error)})
    }     
    }

  bioChange(e) {
    this.setState({bio: e.target.value});
  }


  skillsChange(e, data) {
    const len = data.value.length;
    const skill = data.value.map((v, i) => v);
    this.setState({skills: skill});
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
                    <Form.Field  inline>
                      <label>Skills:</label>
                      <Dropdown placeholder='Skills' multiple selection options={skills} onChange={this.skillsChange}/>
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

const year = [
  { text: '1980', value: '1980' },
  { text: '1981', value: '1981' },
  { text: '1982', value: '1982' },
  { text: '1983', value: '1983' },
  { text: '1984', value: '1984' },
  { text: '1985', value: '1985' },
  { text: '1986', value: '1986' },
  { text: '1987', value: '1987' },
  { text: '1988', value: '1988' },
  { text: '1989', value: '1989' },
  { text: '1990', value: '1990' },
  { text: '1991', value: '1991' },
  { text: '1992', value: '1992' },
  { text: '1993', value: '1993' },
  { text: '1994', value: '1994' },
  { text: '1995', value: '1995' },
  { text: '1996', value: '1996' },
  { text: '1997', value: '1997' },
  { text: '1998', value: '1998' },
  { text: '1999', value: '1999' },
  { text: '2000', value: '2000' },
  { text: '2001', value: '2001' },
  { text: '2002', value: '2002' },
  { text: '2003', value: '2003' },
]

const month = [
  { text: '01', value: '01' },
  { text: '02', value: '02' },
  { text: '03', value: '03' },
  { text: '04', value: '04' },
  { text: '05', value: '05' },
  { text: '06', value: '06' },
  { text: '07', value: '07' },
  { text: '08', value: '08' },
  { text: '09', value: '09' },
  { text: '10', value: '10' },
  { text: '11', value: '11' },
  { text: '12', value: '12' },
]

const day = [
  {text: '01', value: '01' },
  {text: '02', value: '02' },
  {text: '03', value: '03' },
  {text: '04', value: '04' },
  {text: '05', value: '05' },
  {text: '06', value: '06' },
  {text: '07', value: '07' },
  {text: '08', value: '08' },
  {text: '09', value: '09' },
  {text: '10', value: '10' },
  {text: '11', value: '11' },
  {text: '12', value: '12' },
  {text: '13', value: '13' },
  {text: '14', value: '14' },
  {text: '15', value: '15' },
  {text: '16', value: '16' },
  {text: '17', value: '17' },
  {text: '18', value: '18' },
  {text: '19', value: '19' },
  {text: '20', value: '20' },
  {text: '21', value: '21' },
  {text: '22', value: '22' },
  {text: '23', value: '23' },
  {text: '24', value: '24' },
  {text: '25', value: '25' },
  {text: '26', value: '26' },
  {text: '27', value: '27' },
  {text: '28', value: '28' },
  {text: '29', value: '29' },
  {text: '30', value: '30' },
  {text: '31', value: '31' },
]

const skills = [
  {text: 'Java', value : 'Java'},
  {text: 'C', value : 'C'},
  {text: 'C++', value : 'C++'},
  {text: 'Python', value : 'Python'},
]

const gender= [
  { key: 'male', text: 'Male', value: 'male' },
  { key: 'female', text: 'Female', value: 'female' },
]
