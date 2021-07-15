import React, { useState } from "react";

import withRoot from "../../withRoot";

import Login from './Login';
// import Register from './Register';

export default withRoot(() => {
    const [newUser, setNewUser] = useState(true)

    return newUser ? (
      // <Register setNewUser={ setNewUser }/>
      <Login setNewUser={ setNewUser }/>
    ) : (
      <Login setNewUser={ setNewUser }/>
    )


})

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
