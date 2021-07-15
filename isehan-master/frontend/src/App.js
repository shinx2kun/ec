import './App.css';
import ProductList from './components/Main/ProductList'

import React from "react";
import { Query } from "react-apollo";
import { useQuery } from "@apollo/client";
import { gql } from "apollo-boost";
import Container from '@material-ui/core/Container';


const App = () => {
    return(
        <Container>
            <ProductList/>
        </Container>
    )
}


export default App;
