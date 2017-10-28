from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


# Define the WSGI application object
frauk = Flask(__name__)
Bootstrap(frauk)

# Configurations
frauk.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(frauk)

from frauk.views.drinks import drinks
from frauk.views.users import users
from frauk.views.buy import buy
from frauk.views.audits import audits
from frauk.views.stats import stats
from frauk.views.deposit import deposit

frauk.register_blueprint(users)
frauk.register_blueprint(drinks)
frauk.register_blueprint(buy)
frauk.register_blueprint(audits)
frauk.register_blueprint(stats)
frauk.register_blueprint(deposit)
