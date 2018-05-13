from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay
from .model import User

class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )
