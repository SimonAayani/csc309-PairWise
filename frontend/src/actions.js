// from https://auth0.com/blog/secure-your-react-and-redux-app-with-jwt-authentication/
import axios from 'axios';

// There are three possible states for our login
// process and we need actions for each of them
export const LOGIN_REQUEST = 'LOGIN_REQUEST'
export const LOGIN_SUCCESS = 'LOGIN_SUCCESS'
export const LOGIN_FAILURE = 'LOGIN_FAILURE'

function requestLogin(creds) {
  return {
    type: LOGIN_REQUEST,
    isFetching: true,
    isAuthenticated: false,
    creds
  }
}

function receiveLogin(user) {
  return {
    type: LOGIN_SUCCESS,
    isFetching: false,
    isAuthenticated: true,
    jwt_token: user.token,
    id: user.id
  }
}

function loginError(message) {
  return {
    type: LOGIN_FAILURE,
    isFetching: false,
    isAuthenticated: false,
    message
  }
}

export function loginUser(creds) {
  return dispatch => {
    // We dispatch requestLogin to kickoff the call to the API
    dispatch(requestLogin(creds))

    return axios.post('http://165.227.40.205:8000/login/token/', {
        "username": creds.username,
        "password": creds.password
    })
    .then(response => {
      let data = response.data;
      let status = response.status;
      let msg = response.statusText;

      if (status >= 200 && status < 300) {
          localStorage.setItem('jwt_token', data.token);
          dispatch(receiveLogin(data));
      } else {
          dispatch(loginError(msg));
          return Promise.reject(data);
      }
      }).catch(err => console.log("Error: ", err))
  }
}

// Three possible states for our logout process as well.
// Since we are using JWTs, we just need to remove the token
// from localStorage. These actions are more useful if we
// were calling the API to log the user out
export const LOGOUT_REQUEST = 'LOGOUT_REQUEST'
export const LOGOUT_SUCCESS = 'LOGOUT_SUCCESS'
export const LOGOUT_FAILURE = 'LOGOUT_FAILURE'

function requestLogout() {
  return {
    type: LOGOUT_REQUEST,
    isFetching: true,
    isAuthenticated: true
  }
}

function receiveLogout() {
  return {
    type: LOGOUT_SUCCESS,
    isFetching: false,
    isAuthenticated: false
  }
}


// Logs the user out
export function logoutUser() {
  return dispatch => {
    dispatch(requestLogout())
    localStorage.removeItem('jwt_token')
    dispatch(receiveLogout())
  }
}


export const REGISTRATION_REQUEST = 'REGISTRATION_REQUEST'
export const REGISTRATION_SUCCESS = 'REGISTRATION_SUCCESS'
export const REGISTRATION_FAILURE = 'REGISTRATION_FAILURE'

function requestRegistration(info) {
  return {
    type: REGISTRATION_REQUEST,
    isRegistering: true
  }
}

function receiveRegistration() {
  return {
    type: REGISTRATION_SUCCESS,
    isRegistering: false,
  }
}

function registrationError(msg) {
  return {
    type: REGISTRATION_FAILURE,
    isRegistering: false,
    message: msg
  }
}


export function registerUser(user) {
  return dispatch => {
    dispatch(requestRegistration(user));

    axios.post('http://165.227.40.205:8000/registration/', user)
      .then(response => {
        if (response.status >= 200 && response.status < 300) {
          dispatch(receiveRegistration());
        } else {
          dispatch(registrationError(response.statusText));
          return Promise.reject(response);
        }
      })
      .catch(error => console.log(error));
  }
}
