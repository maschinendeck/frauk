from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay
from .model import Product

class ProductSchema(SQLAlchemyObjectType):
    class Meta:
        model = Product
        interfaces = (relay.Node, )
