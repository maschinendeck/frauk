import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Audit, User, Product


class AuditSchema(SQLAlchemyObjectType):
    class Meta:
        model = Audit
        interfaces = (relay.Node, )

class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )

class ProductSchema(SQLAlchemyObjectType):
    class Meta:
        model = Product
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_audits = SQLAlchemyConnectionField(AuditSchema)
    all_users = SQLAlchemyConnectionField(UserSchema)
    all_products = SQLAlchemyConnectionField(ProductSchema)

schema = graphene.Schema(query=Query)
