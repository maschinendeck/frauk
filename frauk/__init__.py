from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

frauk = Flask(__name__)
db = SQLAlchemy(frauk)
ma = Marshmallow(frauk)
frauk.config.from_object('config')

from frauk.users.api import UserAPI, UsersAPI
from frauk.products.api import ProductAPI, ProductsAPI
from frauk.audits.api import AuditsAPI

api = Api(frauk)

api.add_resource(UserAPI, '/users/<int:id>.json', endpoint = 'user')
api.add_resource(UsersAPI, '/users.json', endpoint = 'users')

api.add_resource(ProductAPI, '/products/<int:id>.json', endpoint = 'product')
api.add_resource(ProductsAPI, '/products.json', endpoint = 'products')

api.add_resource(AuditsAPI, '/audits.json', endpoint = 'audits')
