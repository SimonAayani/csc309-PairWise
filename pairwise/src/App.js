import React, { Component } from 'react';
import ProfileCard from "./ProfileCard";
import './App.css';

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			name : "FirstName LastName",
			location : "Toronto",
			picture : "https://chipinworld.com/assets1/images/about-image/no-image.jpg",
			bio : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
			skills : "SQL, C, JavaScript, Java, Python, C++. React, Node.js",
			courses : "CSC301, CSC309, CSC369"
		}
	}
	render() {
		return (
			<div className="Pairwise>">
			<ProfileCard userInfo={this.state} />
			</div>
		);
	}
}

export default App;