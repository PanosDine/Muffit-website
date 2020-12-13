import React, { Component } from "react";
import AboutPage from "./AboutPage";
import ContactPage from "./ContactPage";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";
import CreateOrderPage from "./CreateOrderPage";


export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
        <Router>
            <Switch>
                <Route exact path="/"> 
                    <p>This is the home page</p>
                </Route>
                <Route path="/about" component={AboutPage} />
                <Route path="/contact" component={ContactPage} />
                <Route path="/order" component={CreateOrderPage} />
            </Switch>
        </Router>);
    }
}