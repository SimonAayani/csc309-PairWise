import React from 'react';
import ReactDOM from 'react-dom';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import thunkMiddleware from 'redux-thunk'
import { loadState, saveState } from './localStorage';

import reducers from './reducers.js';
import Main from './components/Main';
import './index.css';

const persistedState = loadState();
const store = createStore(
  reducers,
  persistedState,
  applyMiddleware(thunkMiddleware)
);

store.subscribe(() => {
  saveState(store.getState());
});

ReactDOM.render(
  <Provider store={store}>
    <Main />
  </Provider>,
  document.getElementById('root')
);
