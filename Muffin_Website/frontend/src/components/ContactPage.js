import React, { Component } from "react";

export default class ContactPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            email: '',
            message: ''
        }
    }


    render() {
        return <p>This is the contact page</p>;
    }
}