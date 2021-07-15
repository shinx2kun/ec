import graphene
import graphql_jwt

from users.queries import UsersQuery
from users.mutations import UsersMutation

from backend.queries import ProductQuery, ParentCategoryQuery, ChildCategoryQuery, ProductCompositionTableQuery, ShoppingCartQuery, ShoppingCartItemQuery
from backend.mutations import BackendMutation

class Query(UsersQuery, ProductQuery, ParentCategoryQuery, ChildCategoryQuery, ProductCompositionTableQuery, ShoppingCartQuery, ShoppingCartItemQuery, graphene.ObjectType):
    pass

class Mutation(UsersMutation, BackendMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
