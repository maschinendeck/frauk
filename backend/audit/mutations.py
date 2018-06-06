import graphene
import datetime
from backend import db
from .model import Audit
from .schema import AuditSchema
from ..product.model import Product
from ..user.model import User

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
        product = Product.query.filter_by(id=audit_data.product_id).first()
        user = User.query.filter_by(id=audit_data.user_id).first()
        if user != None and product != None:
            price = product.price
            user.balance = user.balance - price
            user.updated_at = datetime.datetime.now()
            audit = Audit(
                product_id  = audit_data.product_id,
                user_id     = audit_data.user_id,
                difference  = - Product.query
                    .filter_by(id=audit_data.product_id).first().price,
            )
            db.session.add(user)
            db.session.add(audit)
            db.session.commit()
            ok = True
            return CreateProductAudit(audit=audit , ok=ok)
        else:
            return CreateProductAudit(audit = None, ok=False)

class CreateDiffAudit(graphene.Mutation):
    class Arguments:
        audit_data = AuditDiffInput()

    ok = graphene.Boolean()
    audit = graphene.Field(lambda: AuditSchema)

    def mutate(self, info, audit_data=None):
        user = User.query.filter_by(id=audit_data.user_id).first()
        if user != None:
            user.balance = user.balance + audit_data.difference
            user.updated_at = datetime.datetime.now()
            audit = Audit(
                product_id = 0,
                user_id = audit_data.user_id,
                difference = audit_data.difference,
            )
            db.session.add(user)
            db.session.add(audit)
            db.session.commit()
            ok = True
            return CreateDiffAudit(audit=audit , ok=ok)
        else:
            return CreateDiffAudit(audit = None, ok=False)
