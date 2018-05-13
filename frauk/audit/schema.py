from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay
from .model import Audit

class AuditSchema(SQLAlchemyObjectType):
    class Meta:
        model = Audit
        interfaces = (relay.Node, )
