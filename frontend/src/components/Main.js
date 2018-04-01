import React, { Component } from "react";
import PropTypes from 'prop-types';
import { Route, NavLink, BrowserRouter, Redirect } from "react-router-dom";
import { connect } from 'react-redux';
import { loginUser, doAuthentication } from '../actions';
import axios from 'axios';

import Inbox from './Inbox'
import Layout from './Layout';
import Login from './Login';
import LoginPage from './LoginPage';
import NavBar from './NavBar';
import Notifications from './Notifications';
import Registration from './Registration';
import SearchForm from './SearchForm';
import Splash from './Splash';
import MyProfile from './Profile'

import './main.css';

// set axios defaults
axios.defaults.headers.common['Authorization'] = 'JWT ' + localStorage.getItem("jwt-token");

// pure component for restricting access to certain routes
function PrivateRoute ({component: Component, isAuthenticated, ...rest}) {
  return (
    <Route
      {...rest}
      render={(props) => isAuthenticated === true
          ? <Component {...props} />
          : <Redirect to={{pathname: '/login', state: {from: props.location}}} />}
        />
  )
}


class Main extends Component {
  render() {
    const { dispatch, isAuthenticated, isRegistering, errorMessage } = this.props;
    return(
      <BrowserRouter>
        <div>

          <div className="navbar">
            <NavBar isAuthenticated={isAuthenticated} errorMessage={errorMessage} dispatch={dispatch} />
          </div> {/* navbar */}

          <div className="main">
            <Route exact path="/" render={() => isAuthenticated ? <Notifications /> : <Splash />} />
            <Route path="/login" render={() => isAuthenticated ? <Notifications />
                : <LoginPage
                  isAuthenticated={isAuthenticated}
                  errorMessage={errorMessage}
                  dispatch={dispatch}
                />} />
			<Route path="/registration" render={() => isAuthenticated
					? <Notifications />
					: <Registration dispatch={dispatch} isRegistering={isRegistering} />} />
              <PrivateRoute path="/notifications" component={Notifications} isAuthenticated={isAuthenticated}/>
			  <PrivateRoute path="/profile" component={MyProfile} isAuthenticated={isAuthenticated} />
              <PrivateRoute path="/newsearch" component={SearchForm} isAuthenticated={isAuthenticated} />
            </div> {/* closes main */}

          </div>
        </BrowserRouter>
    )
  }
}


Main.propTypes = {
  dispatch: PropTypes.func.isRequired,
  isAuthenticated: PropTypes.bool.isRequired,
  errorMessage: PropTypes.string,
}


// connect the app's props to the redux store
function mapStateToProps(state) {
  const { auth, isRegistering } = state
  const { isAuthenticated, errorMessage } = auth

  return {
    isAuthenticated,
	  errorMessage,
	  isRegistering
  }
}

export default connect(mapStateToProps)(Main)
