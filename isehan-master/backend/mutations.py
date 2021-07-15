import graphene
from django.conf import settings
from graphene import relay, ObjectType
from graphql import GraphQLError
from django.db import transaction
from django.template.loader import render_to_string
from django.core.signing import dumps, loads, SignatureExpired, BadSignature
from graphql_relay import from_global_id

from backend.schema import ShoppingCartNode
from backend.models import ShoppingCartItem, Product


class AddProductToShoppingCart(relay.ClientIDMutation):
    cart = graphene.Field(ShoppingCartNode)
    class Input:
        product = graphene.ID(required=True)
        amount = graphene.Int(required=True)
    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, product, amount):
        shopping_cart = info.context.user.shopping_cart
        cart_item, _ = ShoppingCartItem.objects.get_or_create(
            cart=shopping_cart,
            product=Product.objects.get(pk=from_global_id(product)[1])
        )
        cart_item.amount = amount
        cart_item.save()
        return AddProductToShoppingCart(cart=shopping_cart)

class DeleteProductFromShoppingCart(relay.ClientIDMutation):
    cart = graphene.Field(ShoppingCartNode)
    class Input:
        product = graphene.ID(required=True)
    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, product):
        shopping_cart = info.context.user.shopping_cart
        delete_product = Product.objects.get(pk=from_global_id(product)[1])
        ShoppingCartItem.objects.get(cart=shopping_cart, product=delete_product).delete()
        return AddProductToShoppingCart(cart=shopping_cart)



class BackendMutation(ObjectType):
    add_product_to_cart = AddProductToShoppingCart.Field()
    delete_product_from_cart = DeleteProductFromShoppingCart.Field()