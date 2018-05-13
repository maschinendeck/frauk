import graphene
from frauk.audit.mutations import CreateDiffAudit, CreateProductAudit

class Mutation(graphene.ObjectType):
    create_product_audit = CreateProductAudit.Field()
    create_diff_audit = CreateDiffAudit.Field()
