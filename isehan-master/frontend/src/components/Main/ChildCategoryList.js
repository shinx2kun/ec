import React from "react";
import { Query, Mutation } from "react-apollo";
import { gql } from "apollo-boost";
import {useQuery} from "@apollo/client";

import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Button from "@material-ui/core/Button";

import ProductList from "./ProductList";

import Container from "@material-ui/core/Container";

const ChildCategoryList = ({category}) => {
    const {data, loading, error} = useQuery(SEARCH_PRODUCT_FILTER_CHILD_CATEGORY,{
        variables: {childCategory: category.id},
    })
    if (loading) return "loading"
    if (error) return (console.log(error))
    const products = data.allProducts.edges
    console.log(products)

    return(
        <Container>
            <p>{category.id}</p>
            <p>{category.name}</p>
            {products.map(product=>(
                <div>
                    <p>{product.node.name}</p>
                    <p>{product.node.price}</p>
                </div>
            ))}
        </Container>
    )
}

const SEARCH_PRODUCT_FILTER_CHILD_CATEGORY = gql`
    query searchProductFilteredCategory($childCategory:[ID]){
      allProducts(childCategory:$childCategory){
        edges{
          node{
            name
            price
          }
        }
      }
    }
`

export default ChildCategoryList;

