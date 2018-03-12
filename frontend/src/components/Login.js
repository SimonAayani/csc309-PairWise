import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import "./main.css";

class Login extends Component {
	constructor(props) {
		super(props);

		this.state = {
			username: '',
			password: '',
		}

		this.redirectHome = this.redirectHome.bind(this);
		this.handleUsernameChange = this.handleUsernameChange.bind(this);
		this.handlePasswordChange = this.handlePasswordChange.bind(this);
	}

	handleUsernameChange(e) {
		this.setState({username: e.target.value});
	}

	handlePasswordChange(e) {
		this.setState({password: e.target.value});
	}

	redirectHome() {
		this.props.history.push("/");
	}

	render() {
		const handler = (e) => {
			this.props.handleLogin(e);
			this.redirectHome();
		}

		return (
			<div className="splash">
				<div className="splash-inner">
					<div className="searchForm">
						<h2>Login</h2>
						<form>
							<label>
								<input
									className="fakeSelect"
									name="username"
									onChange={this.handleUsernameChange}
									placeholder="Username"
									type="text"
									value={this.state.username}
								/>
							</label>
							<label>
								<input
									className="fakeSelect"
									name="username"
									onChange={this.handlePasswordChange}
									placeholder="Password"
									type="password"
									value={this.state.password}
								/>
							</label>

							<button onClick={handler}>Log In</button>
						</form>
					</div>
				</div>
			</div>
		)
	}
}

export default withRouter(Login);
