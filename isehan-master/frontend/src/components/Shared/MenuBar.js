import React, {useState} from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import { List, ListItem, ListItemText, Collapse } from "@material-ui/core"
import { ExpandLess, ExpandMore } from "@material-ui/icons";
import {Link} from "react-router-dom";
import Container from '@material-ui/core/Container';
import withStyles from "@material-ui/core/styles/withStyles";
import {useQuery} from "@apollo/client";
import {gql} from "apollo-boost";
const MenuBar = ({ classes }) => {
  const [selected, setSelected] = useState("")
  const { data, loading, error } = useQuery(SEARCH_CATEGORY)
  if (loading) return "loading"
  if (error) return "error"
  const parent_categories = data.allParentCategories.edges
  const handleOpen = (category) => {
    setSelected(category)
  }
  const handleClose = () => {
    setSelected("")
  }
  return (
    <AppBar position="sticky" className={classes.root} onMouseLeave={handleClose}>
      <Container>
        <Toolbar>
          <List component="nav" className={classes.pList}>
          {parent_categories.map(parent_category => (
            <div>
              <ListItem
                  key={parent_category.node.name}
                  component={Link}
                  to={`/${parent_category.node.name}`}
                  className={classes.category_link}
                  onMouseOver={() => handleOpen(parent_category.node.name)}
              >
                <ListItemText primary={parent_category.node.name}/>
                {selected === parent_category.node.name ? <ExpandLess /> : <ExpandMore/>}
              </ListItem>
              <Collapse
                in={selected === parent_category.node.name}
                timeout="auto"
                unmountOnExit
              >
                <List
                  key={parent_category.node.name}
                  component="div"
                  className={classes.cList}
                >
                  {parent_category.node.child.edges.map(child_category=>(
                    <ListItem
                      key={child_category.node.name}
                      component={Link}
                      to={`/${child_category.node.name}`}
                      className={classes.category_link}
                    >
                      <ListItemText primary={child_category.node.name} />
                    </ListItem>
                  ))}
                </List>
              </Collapse>
            </div>
          ))}
          </List>
        </Toolbar>
      </Container>
    </AppBar>
  )
};
const SEARCH_CATEGORY = gql`
  query{
    allParentCategories{
      edges{
        node{
          name
          child{
            edges{
              node{
                name
              }
            }
          }
        }
      }
    }
  }
`
const styles = theme => ({
  root: {
    flexGrow: 1,
    margin: "10px 0",
    padding: 0,
    backgroundColor: "#060D1A"
  },
  grow: {
    flexGrow: 1,
    display: "flex",
    alignItems: "center",
    textDecoration: "none"
  },
  logo: {
    marginRight: theme.spacing.unit,
    fontSize: 45
  },
  faceIcon: {
    marginRight: theme.spacing.unit,
    fontSize: 30,
    color: "white"
  },
  username: {
    color: "white",
    fontSize: 30
  },
  overrides: {
    MuiToolbar: {
      gutters: {
        paddingLeft: 0
      }
    }
  },
  category_link: {
    padding: 10,
    marginLeft: 10,
    marginRight: 10
  },
  pList: {
    display: "flex",
    position: "relative",
  },
  cList: {
    position: "absolute",
    backgroundColor: "#060D1A",
  },
});
export default withStyles(styles)(MenuBar);