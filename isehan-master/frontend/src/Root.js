import React, {useContext, Component} from "react";
import {ApolloProvider, ApolloClient, InMemoryCache, createHttpLink, useQuery} from "@apollo/client";
import { Query } from 'react-apollo'
import { setContext } from "@apollo/client/link/context";
import { gql } from "graphql.macro";
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import withRoot from "./withRoot";

import Header from './components/Shared/Header';
import Loading from './components/Shared/Loading';
import Error from './components/Shared/Error';
import CategoryUrls from './components/Shared/CategoryUrls'

import { AuthProvider } from "./contexts/AuthContext";
// import App from "./App";
// import SearchProductList from "./components/Main/SearchProductList";
// import LoginForm from "./components/Auth/LoginForm";
// import Profile from "./components/Auth/Profile";
import App from './App';
import LoginForm from './components/Auth/LoginForm'
import Profile from './components/Auth/Profile'
import SearchProductList from './components/Main/SearchProductList'
import ParentCategoryList from "./components/Main/ParentCategoryList";

const client = new ApolloClient({
    fetchOptions: {
        credentials: 'include'
    },
    request: operation => {
        const token = localStorage.getItem('authToken') || "";
        operation.setContext({
            headers: {
                Authorization: `JWT ${token}`
            }
        })
    },
    cache: new InMemoryCache(),
    uri: "/graphql/",
    clientState: {
        defaults: {
            isLoggedIn: !!localStorage.getItem('authToken')
        }
    }
});


const Root = () => {
    return (
        <ApolloProvider client={client}>
            <AuthProvider>
                <BrowserRouter>
                    <Header/>
                    <Switch>
                        <Route exact={true} path="/" component={App}/>
                        <Route exact={true} path="/SearchProducts" component={SearchProductList}/>
                        <Route exact={true} path="/Login" component={LoginForm}/>
                        <Route exact={true} path="/Profile/:id" component={Profile}/>
                        <CategoryUrls/>
                    </Switch>
                </BrowserRouter>
            </AuthProvider>
        </ApolloProvider>
    )
}

export default withRoot(Root);