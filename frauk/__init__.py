from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS
from sqlalchemy.ext.declarative import declarative_base

frauk = Flask(__name__)
cors = CORS(frauk, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(frauk)
Base = declarative_base()
Base.query = db.session.query_property()

ma = Marshmallow(frauk)
frauk.config.from_object('config')



from flask_graphql import GraphQLView
from frauk.schema import schema


frauk.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@frauk.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

"""


from frauk.users.api import UserAPI, UsersAPI, UserPaymentAPI, UserTradeAPI
from frauk.products.api import ProductAPI, ProductsAPI
from frauk.audits.api import AuditsAPI

api = Api(frauk)

api.add_resource(UserAPI, '/users/<int:id>.json', endpoint = 'user')
api.add_resource(UsersAPI, '/users.json', endpoint = 'users')
api.add_resource(UserPaymentAPI, '/users/<int:id>/deposit.json', endpoint = 'user.deposit')
api.add_resource(UserPaymentAPI, '/users/<int:id>/pay.json', endpoint = 'user.pay')
api.add_resource(UserTradeAPI, '/users/<int:id>/product.json', endpoint = 'user.product')

api.add_resource(ProductAPI, '/products/<int:id>.json', endpoint = 'product')
api.add_resource(ProductsAPI, '/products.json', endpoint = 'products')

api.add_resource(AuditsAPI, '/audits.json', endpoint = 'audits')
        
        
"""
