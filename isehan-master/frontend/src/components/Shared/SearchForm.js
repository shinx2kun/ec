import React, {useState, useContext} from "react";
import {useMutation, useQuery, gql} from "@apollo/client";
import { useHistory } from "react-router-dom";

import {AuthContext} from "../../contexts/AuthContext";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import {Link} from "react-router-dom";
import RadioIcon from "@material-ui/icons/RadioTwoTone";
import Typography from "@material-ui/core/Typography";
import FaceIcon from "@material-ui/icons/FaceTwoTone";
import IconButton from "@material-ui/core/IconButton";
import ExitToAppIcon from "@material-ui/icons/ExitToApp";
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import SearchIcon from '@material-ui/icons/Search';

import App from "../../App";

import withStyles from "@material-ui/core/styles/withStyles";

const SearchForm = ({ classes }) => {
    const [search, setSearch] = useState("")
    const history = useHistory()

    const handleSubmit = (event) => {
        event.preventDefault()
        history.push(`/SearchProducts?name=${search}`)
    }

    return (
        <div>
            <TextField id="standard-search" label="Search field" type="search" onChange={event=>setSearch(event.target.value)}/>
            <IconButton type="submit" onClick={(event) => handleSubmit(event)}>
                <SearchIcon/>
            </IconButton>
        </div>
    )
}


const styles = theme => ({
});

export default withStyles(styles)(SearchForm);