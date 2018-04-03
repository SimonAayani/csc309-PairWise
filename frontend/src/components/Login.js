import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './Login.css'
import LoginImg from './images/login.png'
import Layout from './Layout';

export default class Login extends Component {

  render() {
    const { errorMessage } = this.props
    return (
        <Layout type="loggedOut">
        <div className="container" >

            <div className = "login_register_img">
            <img src = {LoginImg}/> 
            </div>

            <div id = "logindiv" className="logindiv">

                <div className ="login_info_div">
                        
                            <input type="text" ref='username' placeholder="Username" />
                            <input type="password" ref='password' placeholder="Password" />
                            <input type="submit" name="submit" value="Login" onClick={(event) => this.handleClick(event)}/>
                            {errorMessage &&
                                <p>{errorMessage}</p>
                            }
                            
                        
                        <a href="#register">Don't Have an account? Register here!</a>
                </div>
            </div>  
        </div>
        </Layout>
      )

    //  return (
    //   <Layout type="loggedOut">
    //     <div className='searchForm'>

    //       <h2>Login</h2>
    //       <input type='text' ref='username' className="form-control" placeholder='Username'/>
    //       <input type='password' ref='password' className="form-control" placeholder='Password'/>
    //       <button onClick={(event) => this.handleClick(event)} className="btn btn-primary">
    //         Login
    //       </button>

    //       {errorMessage &&
    //           <p>{errorMessage}</p>
    //       }
    //     </div>
    //   </Layout>
    // )
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
