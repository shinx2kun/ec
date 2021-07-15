from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError

from users.schema import UserNode, ShippingInfoNode

import graphene

class UsersQuery(ObjectType):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    shipping_info = relay.Node.Field(ShippingInfoNode)
    all_shipping_info = DjangoFilterConnectionField(ShippingInfoNode)

    me = graphene.Field(UserNode)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("not logged in!")
        return user