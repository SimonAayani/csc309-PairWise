import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';

class NavBar extends Component {
	render() {
    if (this.props.isLoggedIn) { /* user is logged in */
			return(
				<ul>
				<li id="navbar_logo"><NavLink exact to="/">PairWise</NavLink></li>
				<li>{this.props.loginLink}</li>
				<li><NavLink to="/inbox">Inbox</NavLink></li>
				<li><NavLink to="/groups">Profile</NavLink></li>
				</ul>
			)
    } else { /* user is not logged in */
			return(
				<ul>
				<li id="navbar_logo"><NavLink exact to="/">PairWise</NavLink></li>
				<li>{this.props.loginLink}</li>
				</ul>
			)
		}
	}
};

export default NavBar;
