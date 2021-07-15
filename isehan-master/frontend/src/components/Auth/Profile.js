import React from "react";
import { ApolloProvider, ApolloClient, InMemoryCache, createHttpLink } from "@apollo/client";
import withStyles from "@material-ui/core/styles/withStyles";
import { Query } from "react-apollo";
import { gql } from 'apollo-boost';
import Loading from '../Shared/Loading';
import Error from '../Shared/Error';

const Profile = ({ classes }) => (
  <Query query={GET_USER}>
    {({data, loading, error}) => {
      if (loading) return <Loading />
      if (error) return <Error error={error} />
      const currentUser = data.me
      console.log({currentUser})

      return(
          <div>profile</div>
      )
    }}
  </Query>
)

const GET_USER = gql`
{
  allUsers{
    edges{
      node{
        id
        email
        password
      }
    }
  }
}
`

const styles = theme => ({
  paper: {
    width: "auto",
    display: "block",
    padding: theme.spacing.unit * 2,
    marginLeft: theme.spacing.unit * 3,
    marginRight: theme.spacing.unit * 3,
    marginTop: theme.spacing.unit * 2,
    marginBottom: theme.spacing.unit * 2,
    [theme.breakpoints.up("md")]: {
      width: 650,
      marginLeft: "auto",
      marginRight: "auto"
    }
  },
  card: {
    display: "flex",
    justifyContent: "center"
  },
  title: {
    display: "flex",
    alignItems: "center",
    marginBottom: theme.spacing.unit * 2
  },
  audioIcon: {
    color: "purple",
    fontSize: 30,
    marginRight: theme.spacing.unit
  },
  thumbIcon: {
    color: "green",
    marginRight: theme.spacing.unit
  },
  divider: {
    marginTop: theme.spacing.unit,
    marginBottom: theme.spacing.unit
  }
});

export default withStyles(styles)(Profile);