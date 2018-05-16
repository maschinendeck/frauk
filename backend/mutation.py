import graphene
from .audit.mutations import CreateDiffAudit, CreateProductAudit
from .user.mutations import CreateUser, ModifyUser
from .product.mutations import CreateProduct, ModifyProduct

class Mutation(graphene.ObjectType):
    create_product_audit = CreateProductAudit.Field()
    create_diff_audit = CreateDiffAudit.Field()
    create_user = CreateUser.Field()
    modify_user = ModifyUser.Field()
    create_product = CreateProduct.Field()
    modify_product = ModifyProduct.Field()
