import graphene
from frauk.audit.mutations import CreateDiffAudit, CreateProductAudit
from frauk.user.mutations import CreateUser, ModifyUser

class Mutation(graphene.ObjectType):
    create_product_audit = CreateProductAudit.Field()
    create_diff_audit = CreateDiffAudit.Field()
    create_user = CreateUser.Field()
    modify_user = ModifyUser.Field()
