import { combineReducers } from 'redux'
import {
  LOGIN_REQUEST, LOGIN_SUCCESS, LOGIN_FAILURE, LOGOUT_SUCCESS,
  REGISTRATION_REQUEST, REGISTRATION_SUCCESS, REGISTRATION_FAILURE
} from './actions'

// The auth reducer. The starting state sets authentication
// based on a token being in local storage. In a real app,
// we would also want a util to check if the token is expired.
function auth(state = {
    isFetching: false,
    isAuthenticated: localStorage.getItem('id_token') ? true : false,
    id: 0
  }, action) {
  switch (action.type) {
    case LOGIN_REQUEST:
      return Object.assign({}, state, {
        isFetching: true,
        isAuthenticated: false,
        user: action.creds
      })
    case LOGIN_SUCCESS:
      return Object.assign({}, state, {
        isFetching: false,
        isAuthenticated: true,
        errorMessage: '',
        id: action.id
      })
    case LOGIN_FAILURE:
      return Object.assign({}, state, {
        isFetching: false,
        isAuthenticated: false,
        errorMessage: action.message
      })
    case LOGOUT_SUCCESS:
      return Object.assign({}, state, {
        isFetching: true,
        isAuthenticated: false,
        id: 0
      })
    default:
      return state
  }
}

function registration(state = { isRegistering: false }, action) {
  switch(action.type) {
    case REGISTRATION_REQUEST:
      return Object.assign({}, state, {
        isRegistering: true,
        user: action.user
      })
    case REGISTRATION_SUCCESS:
      return Object.assign({}, state, {
        isRegistering: false,
        errorMessage: ''
      })
    case REGISTRATION_FAILURE:
      return Object.assign({}, state, {
        isRegistering: false,
        errorMessage: action.message
      })
    default:
      return state;
  }
}

// We combine the reducers here so that they
// can be left split apart above
const reducers = combineReducers({
  auth,
  registration
})

export default reducers;
