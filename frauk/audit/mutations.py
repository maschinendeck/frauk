import graphene
from frauk import db
from .model import Audit
from .schema import AuditSchema
from frauk.product.model import Product

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
            difference  = - Product.query
                .filter_by(id=audit_data.product_id).first().price,
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
