import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from .audit.schema import AuditSchema
from .user.schema import UserSchema
from .product.schema import ProductSchema

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_audits = SQLAlchemyConnectionField(AuditSchema)
    all_users = SQLAlchemyConnectionField(UserSchema)
    all_products = SQLAlchemyConnectionField(ProductSchema)
