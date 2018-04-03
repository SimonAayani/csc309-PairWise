import React, {Component} from 'react'
import firebase from './firebase.js'
import './ChatRoom.css'
import profile1 from './images/profile.png'
import profile2 from './images/profile2.png'
// require('./ChatRoom.css')
	
class ChatRoom extends Component{

	constructor(props, context){
		super(props, context)
		this.updateMessage = this.updateMessage.bind(this)
		this.updateUsername = this.updateUsername.bind(this)
		this.submitMessage = this.submitMessage.bind(this)
		this.changeUsername = this.changeUsername.bind(this)
		this.changeRecipient = this.changeRecipient.bind(this)
		this.state = {
			username: 'simon',
			active: '',
			recipient:'',
			pic:'./images/profile.png',
			sender: '',
			message:'',
			messages: [],
			conversations: []
		}
	}
	componentDidMount(){
		console.log('ComponentDidMount')
		firebase.database().ref('messages/').on('value', (snapshot)=> {
			const currentMessages = snapshot.val()

			if(currentMessages !=null){
				this.setState({
					messages: currentMessages
				})

			}
		})
	}

	updateMessage(event){

		console.log('updateMessage:' + event.target.value)
		this.setState({
			message: event.target.value
		})
	}

	updateUsername(event){
		this.setState({
			sender: event.target.value
		})
	}
	changeUsername(event){
		this.setState({
			username: event.target.value
		})
	}
	changeRecipient(event){
		this.setState({
			recipient: event.target.getAttribute("value")
		})
	}

	submitMessage(event){
		const nextMessage = {
			id: this.state.messages.length,
			text: this.state.message,
			username: this.state.username,
			recipient: this.state.recipient
		}
		firebase.database().ref('messages/' + nextMessage.id).set(nextMessage)

	}
	render(){
		this.state.conversations = []
		const Message = this.state.messages.map((message, i) => {
			
			
			if(message.recipient == this.state.username){
				this.state.conversations.push(message)
			}
			if(this.state.recipient != null){
				if(message.recipient == this.state.username || message.username == this.state.username){
					if(message.username == this.state.recipient || message.recipient == this.state.recipient){
						if(message.username != this.state.username){
							return(
								<div key={message.id} className="incoming" >
									<img src={profile2} className="incoming_img"/>
									<p className="name_inc">{message.username}:</p>
				                    <p className="message_inc">{message.text}</p>
								</div>
								
							)
						} else {
							return(
								<div key={message.id} className="outgoing" >
									<img src={profile1} className="outgoing_img"/>
									<p className="name_out">{message.username}</p>
				                    <p className="message_out">{message.text}</p>
								</div>	
							)
						}
					}	
				}
			}
			
		})
		const Conversations = this.state.conversations.map((message, i) => {
			

			return(
				<div key={message.id} className="user" onClick={this.changeRecipient} value={message.username}>
					<img src={profile2} className="user_img"onClick={this.changeRecipient} value={message.username}/>
	                <p className="name"onClick={this.changeRecipient} value={message.username}>{message.username}</p>
	                <p className="course"onClick={this.changeRecipient} value={message.username}>CSC301</p>
				</div>	
			)
		})
		
		const SubmitFields = this.state.conversations.map((message, i) => {
			if(this.state.recipient != '' && i==0){
				return(
					<form key={i} className="messages_container_form">
						<input className="messages_container_text" onChange={this.updateMessage} type="text" placeholder="message"/>
						<input type="button" className="messages_container_submit" onClick={this.submitMessage} value="Submit Message"/>
						
					</form>		
				)
			}
		})

		return(
			<div>
				<div className="messages_container">
					<h2 className="messages_container_h2">{this.state.recipient}</h2>
					<div className="messages">
						{Message}
					</div>
					{SubmitFields}
				</div>
				<div className="conversations">
					{Conversations}
				</div>
			</div>
		)
	}

}
export default ChatRoom