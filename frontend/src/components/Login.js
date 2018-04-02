import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Layout from './Layout';

export default class Login extends Component {

  render() {
    const { errorMessage } = this.props

    return (
      <Layout type="loggedOut">
        <div className='searchForm'>
          <h2>Login</h2>
          <input type='text' ref='username' className="form-control" placeholder='Username'/>
          <input type='password' ref='password' className="form-control" placeholder='Password'/>
          <button onClick={(event) => this.handleClick(event)} className="btn btn-primary">
            Login
          </button>

          {errorMessage &&
              <p>{errorMessage}</p>
          }
        </div>
      </Layout>
    )
  }

  handleClick(event) {
    const username = this.refs.username
    const password = this.refs.password
    const creds = { username: username.value.trim(), password: password.value.trim() }
    this.props.onLoginClick(creds)
  }
}

Login.propTypes = {
  onLoginClick: PropTypes.func.isRequired,
  errorMessage: PropTypes.string
}
