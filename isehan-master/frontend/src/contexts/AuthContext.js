import React, { useEffect, useState } from "react"
import {useMutation, useQuery, gql} from "@apollo/client";
import Error from "../components/Shared/Error";

export const AuthContext = React.createContext({
  isLoggedIn: false,
  useEmail: "",
  handleLogin: () => undefined,
  handleLogout: () => undefined
})

const TOKEN_AUTH_MUTATION = gql`
mutation tokenAuth($email:String!, $password:String!) {
  tokenAuth(email: $email, password: $password){
    token
    payload
    refreshExpiresIn
  }
}
`

const VERIFY_TOKEN_MUTATION = gql`
mutation VerifyToken($token: String){
    verifyToken(token: $token){
      payload
    }
  }
`

export const AuthProvider = props => {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [userEmail, setUserEmail] = useState("")

  const [verifyTokenMutation] = useMutation(
    VERIFY_TOKEN_MUTATION,
      {
        onCompleted: data => {
          setUserEmail(data.verifyToken.payload.email)
          setIsLoggedIn(true)
        }
      }
  )
  const verifyToken = (token) => {
    verifyTokenMutation({
      variables: {
        token: token
      }
    })
  }
  useEffect(() => {
    const token = localStorage.getItem("authToken")
    if (token && !isLoggedIn) {
      verifyToken(token)
    }
  })

  const [authTokenMutation] = useMutation(TOKEN_AUTH_MUTATION, {
    onCompleted(data) {
      setUserEmail(data.tokenAuth.payload.email)
      setIsLoggedIn(true)
      localStorage.setItem("authToken", data.tokenAuth.token)
    },
    onError(error){
      setUserEmail("")
      setIsLoggedIn(false)
    }
  })
  const handleLogin = (email, password) => {
    authTokenMutation({
      variables: {
        email: email,
        password: password
      }
    })
  }
  const handleLogout = () => {
    localStorage.removeItem("authToken")
    setUserEmail("")
    setIsLoggedIn(false)
  }

  const context = {
    isLoggedIn,
    userEmail,
    handleLogin,
    handleLogout,
  }

  return (
      <AuthContext.Provider value={context}>
        {props.children}
      </AuthContext.Provider>
  )
}
