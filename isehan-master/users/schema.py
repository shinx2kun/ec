import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from users.models import User, ShippingInfo
from users.dataloaders import shipping_info_loader


class ShippingInfoNode(DjangoObjectType):
    class Meta:
        model = ShippingInfo
        filter_fields = ['user', 'name']
        interfaces = (relay.Node, )


class ShippingInfoConnection(relay.Connection):
    class Meta:
        node = ShippingInfoNode


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'email': ['exact', 'icontains', 'istartswith'],
            'is_staff': ['exact'],
            'is_active': ['exact'],
        }
        interfaces = (relay.Node, )

    shippinginfo_set = relay.ConnectionField(ShippingInfoConnection)

    def resolve_shippinginfo_set(root, info, **kwargs):
        return shipping_info_loader.load(root.id)
