import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Login from './Login'
import Logout from './Logout'
import { loginUser, logoutUser } from '../actions'

export default class LoginPage extends Component {

  render() {
    const { dispatch, isAuthenticated, errorMessage } = this.props

    return (
      <div className='splash'>
      <div className='splash-inner'>

            {!isAuthenticated &&
              <Login
                errorMessage={errorMessage}
                onLoginClick={ creds => dispatch(loginUser(creds)) }
              />
            }

            {isAuthenticated &&
              <Logout onLogoutClick={() => dispatch(logoutUser())} />
            }

          </div>
        </div>
    )
  }

}

LoginPage.propTypes = {
  dispatch: PropTypes.func.isRequired,
  isAuthenticated: PropTypes.bool.isRequired,
  errorMessage: PropTypes.string
}
