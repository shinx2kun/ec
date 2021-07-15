import React, {useContext, useState} from "react";
import { Mutation } from 'react-apollo'
import { gql } from 'apollo-boost'

import { useHistory } from "react-router-dom";

import withStyles from "@material-ui/core/styles/withStyles";
import Typography from "@material-ui/core/Typography";
import Avatar from "@material-ui/core/Avatar";
import FormControl from "@material-ui/core/FormControl";
import Paper from "@material-ui/core/Paper";
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import Button from "@material-ui/core/Button";
import Lock from "@material-ui/icons/Lock";
import Gavel from "@material-ui/icons/Gavel";
import Dialog from "@material-ui/core/Dialog";
import DialogTitle from "@material-ui/core/DialogTitle";
import VerifiedUserTwoTone from "@material-ui/icons/VerifiedUserTwoTone";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogActions from "@material-ui/core/DialogActions";

import Error from "../Shared/Error";
import {AuthContext} from "../../contexts/AuthContext";


const LoginForm = ({ classes, setNewUser }) => {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const authContext = useContext(AuthContext)

  const history = useHistory()

  // const handleSubmit = async (event, tokenAuth, client) => {
  //   event.preventDefault();
  //   const res = await tokenAuth();
  //   localStorage.setItem('authToken', res.data.tokenAuth.token);
  //   client.writeData({ data: { isLoggedIn: true }})
  // };
  //
  return (
      <div className={classes.root}>
        <Paper className={classes.paper}>
          <Avatar className={classes.avatar}>
            <Lock />
          </Avatar>
          <Typography variant="title">
            Login as Existing User
          </Typography>
          {/*<Mutation*/}
          {/*    mutation={LOGIN_MUTATION}*/}
          {/*    variables={{ email, password }}*/}
          {/*    onCompleted={data=>{console.log({data})}}*/}
          {/*>*/}
          {/*  {(tokenAuth, { loading, error, called, client }) => {*/}
          {/*    return (*/}
          {/*        <form onSubmit={event => handleSubmit(event, tokenAuth, client)} className={classes.form}>*/}
          {/*          <FormControl margin="normal" required fullWidth >*/}
          {/*            <InputLabel htmlFor="email">Email</InputLabel>*/}
          {/*            <Input id="email" onChange={event => setEmail(event.target.value)} />*/}
          {/*          </FormControl>*/}
          {/*          <FormControl margin="normal" required fullWidth >*/}
          {/*            <InputLabel htmlFor="password">Password</InputLabel>*/}
          {/*            <Input id="password" type="password" onChange={event => setPassword(event.target.value)} />*/}
          {/*          </FormControl>*/}
          {/*          <Button*/}
          {/*              type="submit"*/}
          {/*              className={classes.submit}*/}
          {/*              fullWidth*/}
          {/*              variant="contained"*/}
          {/*              color="primary"*/}
          {/*              disabled={ loading  || !email.trim() || !password.trim() }*/}
          {/*          >*/}
          {/*            { loading ? "Logging in..." : "Login"}*/}
          {/*          </Button>*/}
          {/*          <Button*/}
          {/*              color="secondary"*/}
          {/*              variant="outlined"*/}
          {/*              fullWidth*/}
          {/*              onClick={() => setNewUser(true)}*/}
          {/*          >*/}
          {/*            New user? Register here*/}
          {/*          </Button>*/}

                    { /*Error Handling*/  }
            {/*        { error && <Error error={error} /> }*/}

            {/*      </form>*/}
            {/*  );*/}
            {/*}}*/}
          {/*</Mutation>*/}
            <form
                onSubmit={event => {
                  authContext.handleLogin(email, password)
                  history.push("/")
                }}
                className={classes.form}
            >
              <FormControl margin="normal" required fullWidth >
                <InputLabel htmlFor="email">Email</InputLabel>
                <Input id="email" onChange={event => setEmail(event.target.value)} />
              </FormControl>
              <FormControl margin="normal" required fullWidth >
                <InputLabel htmlFor="password">Password</InputLabel>
                <Input id="password" type="password" onChange={event => setPassword(event.target.value)} />
              </FormControl>
              <Button
                  type="submit"
                  className={classes.submit}
                  fullWidth
                  variant="contained"
                  color="primary"
                  disabled={ !email.trim() || !password.trim() }
              >
                {"Login"}
              </Button>
              <Button
                  color="secondary"
                  variant="outlined"
                  fullWidth
                  onClick={() => setNewUser(true)}
              >
                New user? Register here
              </Button>
            </form>
        </Paper>
      </div>
  );
};

const LOGIN_MUTATION = gql`
  mutation($email:String!, $password:String!){
    tokenAuth(email: $email, password: $password){
      token
    }
  }
`



const styles = theme => ({
  root: {
    width: "auto",
    display: "block",
    marginLeft: theme.spacing.unit * 3,
    marginRight: theme.spacing.unit * 3,
    [theme.breakpoints.up("md")]: {
      width: 400,
      marginLeft: "auto",
      marginRight: "auto"
    }
  },
  paper: {
    marginTop: theme.spacing.unit * 8,
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    padding: theme.spacing.unit * 2
  },
  title: {
    marginTop: theme.spacing.unit * 2,
    color: theme.palette.secondary.main
  },
  avatar: {
    margin: theme.spacing.unit,
    backgroundColor: theme.palette.primary.main
  },
  form: {
    width: "100%",
    marginTop: theme.spacing.unit
  },
  submit: {
    marginTop: theme.spacing.unit * 2,
    marginBottom: theme.spacing.unit * 2
  }
});

export default withStyles(styles)(LoginForm);
