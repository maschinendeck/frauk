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


import graphene
from flask_graphql import GraphQLView
from .mutation import Mutation
from .query import Query

frauk.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=graphene.Schema(query=Query, mutation=Mutation),
        graphiql=True # for having the GraphiQL interface
    )
)

@frauk.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
