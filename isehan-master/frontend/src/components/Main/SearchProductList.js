import React from "react";
import { Mutation } from "react-apollo";
import { gql } from "apollo-boost";
import { useLocation } from "react-router-dom";

import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Button from "@material-ui/core/Button";
import ProductList from "./ProductList";
import {useQuery} from "@apollo/client";
import Container from '@material-ui/core/Container';

const SearchProductList = () => {
    const { search } = useLocation()
    const params = new URLSearchParams(search)
    const { data, loading, error } = useQuery(SEARCH_PRODUCTS, {
        variables: { name_Icontains: params.get("name") }
    })
    if (loading) return "loading"
    if (error) return "error"
    const products = data.allProducts.edges

    if (products==false){
        return(
            <Container>
                <div>
                    <p>{`「${params.get("name")}」 に該当する商品はありません。`}</p>
                </div>
            </Container>
        )
    } else {
        return(
            <Container>
                <div>
                    {products.map(product => (
                        <List key={product.node.id}>
                            <p>{product.node.name}</p>
                            <p>{product.node.price}</p>
                        </List>
                    ))}
                </div>
            </Container>
        )
    }
}

const SEARCH_PRODUCTS = gql`
    query searchProducts($name_Icontains:String){
      allProducts(name_Icontains: $name_Icontains){
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


export default SearchProductList;
