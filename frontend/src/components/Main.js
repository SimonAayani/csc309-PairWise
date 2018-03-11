import React, { Component } from "react";
import { Route, NavLink, BrowserRouter } from "react-router-dom";

import Dashboard from './Dashboard';
import Login from './Login';
import NavBar from './NavBar';
/*import SearchForm from './SearchForm';*/
import Splash from './Splash';

import './main.css';

class Main extends Component {
    constructor(props) {
        super(props);

        // for now, we'll model user authentication with a boolean state variable
        this.state = {isLoggedIn: false};

        // bindings
        this.handleLogin = this.handleLogin.bind(this);
        this.handleLogout = this.handleLogout.bind(this);
    }

    // functions for toggling Login/Logout
    handleLogin(e) {
        e.preventDefault();
        this.setState({isLoggedIn: true});
    }

    handleLogout(e) {
        e.preventDefault();
        this.setState({isLoggedIn: false});
    }

    render() {
        let loginLink = null;
        loginLink =
            <LoginLink
                isLoggedIn={this.state.isLoggedIn}
                handleLogin={this.handleLogin}
                handleLogout={this.handleLogout}
            />

            return(
                <BrowserRouter>
                    <div className="container">

                        <div className="navbar">
                            <NavBar isLoggedIn={this.state.isLoggedIn} loginLink={loginLink} />
                        </div> {/* navbar */}

                            <div className="main">
                                <Route exact path="/" render={() => this.state.isLoggedIn ? <Dashboard /> : <Splash />} />
                                <Route path="/login" render={() => <Login handleLogin={this.handleLogin} /> } />
                                <Route path="/splash" component={Splash}/>
                                <Route path="/dashboard" component={Dashboard}/>
                                <Route path="/logout" component={Splash} />
                            </div> {/* closes main */}

                    </div>
                </BrowserRouter>
            )
    }
}

class LoginLink extends Component {
    render() {
        if (this.props.isLoggedIn) {
            return(<NavLink to="/logout" onClick={this.props.handleLogout}>Log Out</NavLink>)
        } else {
            return(<NavLink to="/login">Log In</NavLink>)
        }
    }
}


export default Main;
