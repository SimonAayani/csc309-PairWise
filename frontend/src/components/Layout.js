import React from 'react';
import Sidebar from './Sidebar';
import './Dashboard.css';

const Layout = ({ children, type }) => (
    type == 'loggedIn' ? (
        <div className="dashContainer">
            <div id="sideContainer">
                <Sidebar />
            </div>
            <div id="contentContainer">
                {children}
            </div>
        </div>
    ) : (
        <div className="splash">
            {children}
        </div>
    )
);

export default Layout;
