import React, {useContext} from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import RadioIcon from "@material-ui/icons/RadioTwoTone";
import FaceIcon from "@material-ui/icons/FaceTwoTone";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import {Link, Switch} from 'react-router-dom'
import Button from "@material-ui/core/Button";
import Container from '@material-ui/core/Container';

import App from "../../App";
// import Signout from "../Auth/Signout";
import SearchFormm from "./SearchForm";
import MenuBar from "./MenuBar";
import { AuthContext } from "../../contexts/AuthContext";
import {UserContext} from "../../Root";
import { BrowserRouter, Route } from 'react-router-dom'

const LoginCheck = ({ classes }) => {
    const { isLoggedIn, userEmail, handleLogout } = useContext(AuthContext)

    if (!isLoggedIn) {
        return(
            <div>
                {!isLoggedIn && (
                  <Link to={"/Login"}>
                    <Typography variant="headline" color="inherit" noWrap>
                      Login
                    </Typography>
                  </Link>
                )}
            </div>
     )
    } else {
        return(
            <div>
                {userEmail && (
                  <Link to={`/Profile/${userEmail}`}>
                    <FaceIcon className={classes.faceIcon} />
                    <Typography variant="headline" className={classes.email} noWrap>
                      { userEmail }
                    </Typography>
                  </Link>
                )}
                <IconButton onClick={handleLogout} color="inherit">
                  <ExitToAppIcon />
                </IconButton>
            </div>
        )
    }
}

const styles = theme => ({
  logo: {
    marginRight: theme.spacing.unit,
    fontSize: 45
  },
  faceIcon: {
    marginRight: theme.spacing.unit,
    fontSize: 30,
    color: "black"
  },
  username: {
    color: "white",
    fontSize: 30
  }
});

export default withStyles(styles)(LoginCheck);