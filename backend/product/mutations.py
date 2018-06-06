import graphene
import datetime
from backend import db
from .model import Product
from .schema import ProductSchema


class ModifyProductInput(graphene.InputObjectType):
    product_id = graphene.Int(required=True)
    name = graphene.String()
    price = graphene.Int()
    bottle_size_l = graphene.Float()
    caffeine_mg = graphene.Int()
    active = graphene.Boolean()

class ModifyProduct(graphene.Mutation):
    class Arguments:
        product_data = ModifyProductInput()
    
    ok = graphene.Boolean()
    product = graphene.Field(lambda : ProductSchema)

    def mutate(self, info, product_data=None):
        if product_data:
            product = Product.query.filter_by(id=product_data.product_id).first()
            if product == None:
                return ModifyProduct(product=product, ok=False)
            changed = False
            if "name" in product_data:
                product.name = product_data.name
                changed = True
            if "price" in product_data:
                product.price = product_data.price
                changed = True
            if "bottle_size_l" in product_data:
                product.bottle_size_l = product_data.bottle_size_l
                changed = True
            if "caffeine_mg" in product_data:
                product.caffeine_mg = product_data.caffeine_mg
                changed = True
            if "active" in product_data:
                product.active = product_data.active
                changed = True
            if changed:
                product.updated_at = datetime.datetime.now()
                db.session.add(product)
                db.session.commit()
                ok = True
                return ModifyProduct(product=product, ok=ok)
            else:
                ok = False
                return ModifyProduct(product=product, ok=ok)

class CreateProductInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Int(required=True)
    bottle_size_l = graphene.Float()
    caffeine_mg = graphene.Int()
    active = graphene.Boolean()

class CreateProduct(graphene.Mutation):
    class Arguments:
        product_data = CreateProductInput()

    ok = graphene.Boolean()
    product = graphene.Field(lambda: ProductSchema)

    def mutate(self, info, product_data=None):
        if product_data:
            product = Product(name=product_data.name, price = product_data.price)
            if "bottle_size_l" in product_data:
                product.bottle_size_l = product_data.bottle_size_l
            if "caffeine_mg" in product_data:
                product.caffeine_mg = product_data.caffeine_mg
            if "active" in product_data:
                product.active = product_data.active
            db.session.add(product)
            db.session.commit()
            ok = True
            return CreateProduct(product=product , ok=ok)
        else:
            return CreateProduct(product=None, ok=False)
