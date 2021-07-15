from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from backend.schema import ProductNode, ParentCategoryNode, ChildCategoryNode, ProductCompositionTableNode, ShoppingCartNode, ShoppingCartItemNode


class ProductQuery(ObjectType):
    all_products = DjangoFilterConnectionField(ProductNode)

class ParentCategoryQuery(ObjectType):
    all_parent_categories = DjangoFilterConnectionField(ParentCategoryNode)

class ChildCategoryQuery(ObjectType):
    all_child_categories = DjangoFilterConnectionField(ChildCategoryNode)

class ProductCompositionTableQuery(ObjectType):
    all_product_descriptions = DjangoFilterConnectionField(ProductCompositionTableNode)

class ShoppingCartQuery(ObjectType):
    shopping_cart = DjangoFilterConnectionField(ShoppingCartNode)

class ShoppingCartItemQuery(ObjectType):
    shopping_cart_item = DjangoFilterConnectionField(ShoppingCartItemNode)
