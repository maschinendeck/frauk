import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Audit, User, Product
from frauk import db


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

class AuditProductInput(graphene.InputObjectType):
    product_id = graphene.Int(required=True)
    user_id = graphene.Int(required=True)

class AuditDiffInput(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    difference = graphene.Int(required=True)

class CreateProductAudit(graphene.Mutation):
    class Arguments:
        audit_data = AuditProductInput()

    ok = graphene.Boolean()
    audit = graphene.Field(lambda: AuditSchema)

    def mutate(self, info, audit_data=None):
        audit = Audit(
            product_id  = audit_data.product_id,
            user_id     = audit_data.user_id,
            difference  = - Product.query.filter_by(id=audit_data.product_id).first().price,
        )
        db.session.add(audit)
        db.session.commit()
        ok = True
        return CreateProductAudit(audit=audit , ok=ok)

class CreateDiffAudit(graphene.Mutation):
    class Arguments:
        audit_data = AuditDiffInput()

    ok = graphene.Boolean()
    audit = graphene.Field(lambda: AuditSchema)

    def mutate(self, info, audit_data=None):
        audit = Audit(
            product_id = 0,
            user_id = audit_data.user_id,
            difference = audit_data.difference,
        )
        db.session.add(audit)
        db.session.commit()
        ok = True
        return CreateDiffAudit(audit=audit , ok=ok)

class Mutation(graphene.ObjectType):
    create_product_audit = CreateProductAudit.Field()
    create_diff_audit = CreateDiffAudit.Field()

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_audits = SQLAlchemyConnectionField(AuditSchema)
    all_users = SQLAlchemyConnectionField(UserSchema)
    all_products = SQLAlchemyConnectionField(ProductSchema)


schema = graphene.Schema(query=Query, mutation=Mutation)
