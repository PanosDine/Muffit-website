import React, { Component } from 'react';
import { Button, Grid, Typography, TextField, FormControl, FormHelperText, 
    Radio, RadioGroup, FormControlLabel } from "@material-ui/core";
import { Link } from "react-router-dom";


export default class CreateOrderPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            address: '',
            date: '',
            client: ''
        };

        this.handleAddressChange = this.handleAddressChange.bind(this)
        this.handleDateTimeChange = this.handleDateTimeChange.bind(this)
        this.handleClientChange = this.handleClientChange.bind(this)
        this.handleOrderButtonPressed = this.handleOrderButtonPressed.bind(this)
    }

    handleAddressChange(e) {
        this.setState({
            address: e.target.value
        });
    }

    handleDateTimeChange(e) {
        this.setState({
            date: e.target.value 
        });
    }

    handleClientChange(e) {
        this.setState({
            client: e.target.value
        });
    }

    handleOrderButtonPressed() {
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/json' },
            body: JSON.stringify({
                delivery_address: this.state.address,
                delivery_date: this.state.dateTime,
                customer: this.state.client
            }),
        };
        fetch("/api/create-order", requestOptions)
        .then((response) => response.json())
        .then((data) => console.log(data));
    }

    render() {
        return <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <Typography component='h4' variant='h4'>
                    Make an order
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl component="fieldset">
                    <FormHelperText>
                        <div align='center'>Enter your details</div>
                    </FormHelperText>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField 
                        required={true} 
                        type="text"
                        onChange={this.handleAddressChange}
                        inputProps={{
                            min: 1,
                            style: { align: "center"}
                        }}
                    />
                    <FormHelperText>
                        <div align="center">Delivery Address</div>
                    </FormHelperText>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField 
                        id="datetime-local"
                        label="Delivery date and time"
                        required={true} 
                        type="datetime-local"
                        
                        onChange={this.handleDateTimeChange}
                        InputLabelProps={{
                            shrink: true,
                        }}
                        inputProps={{
                            min: 1,
                            style: { align: "center"}
                        }}
                    />
                    <FormHelperText>
                        <div align="center">Delivery Date And Time</div>
                    </FormHelperText>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField 
                        required={true} 
                        type="text"
                        onChange={this.handleClientChange}
                        inputProps={{
                            min: 1,
                            style: { align: "center"}
                        }}
                    />
                    <FormHelperText>
                        <div align="center">Name</div>
                    </FormHelperText>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <Button 
                color="primary" 
                variant="contained" 
                onClick={this.handleOrderButtonPressed}>
                Make an Order
                </Button>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="secondary" variant="contained" to="/" component={Link}>
                Back
                </Button>
            </Grid>
        </Grid>;
    }
}