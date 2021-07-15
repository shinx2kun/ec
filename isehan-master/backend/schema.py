import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from backend.models import Product, ParentCategory, ChildCategory, ProductCompositionTable, ShoppingCart, ShoppingCartItem




class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {'name': ['icontains'],'price':[],'parent_category':['exact'],'child_category':['exact']}
        interfaces = (relay.Node,)

class ParentCategoryNode(DjangoObjectType):
    class Meta:
        model = ParentCategory
        filter_fields = '__all__'
        interfaces = (relay.Node,)

class ChildCategoryNode(DjangoObjectType):
    class Meta:
        model = ChildCategory
        filter_fields = '__all__'
        interfaces = (relay.Node,)

class ProductCompositionTableNode(DjangoObjectType):
    class Meta:
        model = ProductCompositionTable
        filter_fields = '__all__'
        interfaces = (relay.Node,)

class ShoppingCartNode(DjangoObjectType):
    class Meta:
        model = ShoppingCart
        filter_fields = '__all__'
        interfaces = (relay.Node,)

class ShoppingCartItemNode(DjangoObjectType):
    class Meta:
        model = ShoppingCartItem
        filter_fields = '__all__'
        interfaces = (relay.Node,)


