GET_USER_QUERY = '''
query GetUser($id: ID!) {
  user(id: $id) {
    id
    email
    password
    lastLogin
    isStaff
    isSuperuser
    isActive
    dateJoined
    shippinginfoSet {
      edges {
        node {
          id
          name
          zipcode
          address1
          address2
          address3
        }
      }
    }
  }
}
'''

GET_USERS_QUERY = '''
query GetUserList($cursor: String, $email: String, $isStaff: Boolean, $isActive: Boolean) {
  allUsers(first: 10, after: $cursor, email_Icontains: $email, isStaff: $isStaff, isActive: $isActive) {
    pageInfo {
      endCursor
      hasNextPage
    }
    edges {
      node {
        id
        email
        password
        lastLogin
        isStaff
        isSuperuser
        isActive
        dateJoined
        shippinginfoSet {
          edges {
            node {
              id
              name
              zipcode
              address1
              address2
              address3
            }
          }
        }
      }
    }
  }
}
'''

CREATE_USER_MUTATION = '''
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    user {
      id
      email
      password
      lastLogin
      isStaff
      isSuperuser
      isActive
      dateJoined
    }
  }
}
'''

ACTIVATE_USER_MUTATION = '''
mutation ActivateUser($input: ActivateUserInput!) {
  activateUser(input: $input) {
    user {
      id
      email
      password
      lastLogin
      isStaff
      isSuperuser
      isActive
      dateJoined
    }
  }
}
'''

CHANGE_USER_PASSWORD_MUTATION = '''
mutation ChangeUserPassword($input: ChangeUserPasswordInput!) {
  changeUserPassword(input: $input) {
    user {
      id
      email
      password
      lastLogin
      isStaff
      isSuperuser
      isActive
      dateJoined
    }
  }
}
'''

DEACTIVATE_USER_MUTATION = '''
mutation DeactivateUser($input: DeactivateUserInput!) {
  deactivateUser(input: $input) {
    user {
      id
      email
      password
      lastLogin
      isStaff
      isSuperuser
      isActive
      dateJoined
    }
  }
}
'''

DELETE_USER_MUTATION = '''
mutation DeleteUser($input: DeleteUserInput!) {
  deleteUser(input: $input) {
    ok
  }
}
'''