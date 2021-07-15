import withStyles from "@material-ui/core/styles/withStyles";
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import React from "react";

import App from '../../App';
import LoginForm from '../Auth/LoginForm'
import Profile from '../Auth/Profile'
import ParentCategoryList from '../Main/ParentCategoryList'
import ChildCategoryList from '../Main/ChildCategoryList'
import SearchProductList from '../Main/SearchProductList'

import {useQuery} from "@apollo/client";
import {gql} from "graphql.macro";


const CategoryUrls = ({ classes }) => {
    const {data, loading, error} = useQuery(SEARCH_CATEGORY)
    if (loading) return "loading"
    if (error) return "error"
    const parent_categories = data.allParentCategories.edges
    const child_categories = data.allChildCategories.edges

    const parent_category = parent_categories.map(parent_category => (
        <Route exact={true} path={`/${parent_category.node.name}`}>
            <ParentCategoryList category={parent_category.node}/>
        </Route>
    ))
    const child_category = child_categories.map(child_category => (
        <Route exact={true} path={`/${child_category.node.name}`}>
            <ChildCategoryList category={child_category.node}/>
        </Route>
    ))


    return(
        <div>
            {parent_category}
            {child_category}
        </div>
    )
}

const SEARCH_CATEGORY = gql`
    query{
      allParentCategories {
        edges {
          node {
            id
            name
          }
        }
      }
      allChildCategories {
        edges {
          node {
            id
            name
          }
        }
      }
    }
`

const styles = theme => ({

});


export default withStyles(styles)(CategoryUrls);