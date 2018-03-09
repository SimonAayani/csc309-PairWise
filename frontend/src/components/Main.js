import React, { Component } from "react";
import {
    BrowserRouter,
    Route,
} from "react-router-dom";
import Dashboard from './Dashboard';
import Login from './Login';
import PrivateRoute from './PrivateRoute';

class Main extends Component {
    constructor(props) {

        super(props);
        this.state = {isAuthed: false};

        this.logIn = this.logIn.bind(this);
        this.logOut = this.logOut.bind(this);
        this.getIsAuthed = this.getIsAuthed(this);
    }

    logIn() {
        this.setState({isAuthed: true});
        console.log("changed to true");
    }

    logOut() {
        this.setState({isAuthed: false});
    }

    getIsAuthed() {
        return this.state.isAuthed;
    }

    render() {
        const isAuthed = this.state.isAuthed;
        return (
            <BrowserRouter>
            <div>
            <Route path='/' exact render={
                isAuthed ? <h3>welcome back</h3>
                         : <button onClick={this.logIn}>Log In</button>
            }  />
            <PrivateRoute isAuthed={this.state.isAuthed} path='/dashboard' component={Dashboard} />
            </div>
            </BrowserRouter>
        )
    }
}




export default Main;
