import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from frauk.audit.schema import AuditSchema
from frauk.user.schema import UserSchema
from frauk.product.schema import ProductSchema

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_audits = SQLAlchemyConnectionField(AuditSchema)
    all_users = SQLAlchemyConnectionField(UserSchema)
    all_products = SQLAlchemyConnectionField(ProductSchema)
