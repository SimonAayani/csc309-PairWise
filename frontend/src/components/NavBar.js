import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import { loginUser, logoutUser } from '../actions'

class NavBar extends Component {

	render() {
    const { dispatch, isAuthenticated, errorMessage } = this.props
    if (isAuthenticated) { /* user is logged in */
			return(
				<ul>
				<li id="navbar_logo"><NavLink exact to="/">PairWise</NavLink></li>
        <li><NavLink to="/" onClick={() => dispatch(logoutUser())}>Logout</NavLink></li>
        <li><NavLink to="/chatroom">Inbox</NavLink></li>
				<li><NavLink to="/profile">Profile</NavLink></li>
				</ul>
			)
    } else { /* user is not logged in */
			return(
				<ul>
				<li id="navbar_logo"><NavLink exact to="/">PairWise</NavLink></li>
        <li><NavLink to="/login">Login</NavLink></li>
        <li><NavLink to="/chatroom">Register</NavLink></li>
				</ul>
			)
		}
	}
};

export default NavBar;
