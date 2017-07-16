from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


# Define the WSGI application object
app = Flask(__name__)
Bootstrap(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.views.drinks import drinks
from app.views.users import users
from app.views.buy import buy
from app.views.audits import audits
from app.views.stats import stats

app.register_blueprint(users)
app.register_blueprint(drinks)
app.register_blueprint(buy)
app.register_blueprint(audits)
app.register_blueprint(stats)
