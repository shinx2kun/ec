import React from "react";
import { Query, Mutation } from "react-apollo";
import { gql } from "apollo-boost";

import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Button from "@material-ui/core/Button";
import {useQuery} from "@apollo/client";
import Container from "@material-ui/core/Container";


const ProductList = () => {
    const {data, loading, error} = useQuery(ALL_PRODUCTS)
    if (loading) return "loading"
    if (error) return "error"
    const products = data.allProducts.edges

    return (
        <div>
            {products.map(product => (
                <List key={product.node.id}>
                    <p>{product.node.name}</p>
                    <p>{product.node.price}</p>
                </List>
            ))}
        </div>
    )
}

const ALL_PRODUCTS = gql`
    query{
      allProducts{
        edges{
          node{
            id
            price
            name
          }
        }
      }
    }
`

export default ProductList;