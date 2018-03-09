import React from 'react';
import { Route, Redirect } from 'react-router-dom';

function PrivateRoute({component: Component, isAuthed, ...rest}) {
  return(
    <Route
      {...rest}
      render={props => ( isAuthed === true
        ? <Component {...props} />
        : <Redirect to={{pathname: '/login', state: {from: props.location}}} />
      )}
    />
  )}

export default PrivateRoute;
