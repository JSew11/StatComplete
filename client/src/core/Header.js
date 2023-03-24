import React, { Component } from "react";

class Header extends Component {
    render() {
        return (
            <div className="container-fluid p-2">
                <div className="row align-items-center">
                    <div className="col">
                    </div>
                    <div className="col-8 text-center">
                        <h1>StatComplete</h1>
                    </div>
                    <div className="col">
                        <a className="btn btn-secondary">Sign In</a>
                    </div>
                </div>
            </div>
        );
    }
}

export default Header;