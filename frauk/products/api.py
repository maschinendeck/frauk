from frauk import db
from flask_restful import Resource
from flask import request
from .model import Product, ProductSchema
from sqlalchemy import update

productSchema = ProductSchema()
productsSchema = ProductSchema(many=True)

class ProductAPI(Resource):

    def get(self, id):
        product = Product.query.get(id)
        return productSchema.dump(product).data

    def delete(self, id):
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return {},200
        else:
            return {},404

    def patch(self, id):
        data = request.get_json()
        errors = productSchema.load(data, partial=True).errors
        if errors:
            return errors, 400
        else:
            ex = update(Product.__table__).where(Product.id == id).values(data)
            db.session.execute(ex)
            db.session.commit()
            return self.get(id)
        
        

class ProductsAPI(Resource):

    def get(self):
        products = Product.query.all()
        return productsSchema.dump(products).data

    def post(self):
        product = productSchema.load(request.get_json())
        if product.errors:
            return product.errors
        else:
            db.session.add(product.data)
            db.session.commit()
            return productSchema.dump(product.data)
