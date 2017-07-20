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

from frauk.views.drinks import drinks
from frauk.views.users import users
from frauk.views.buy import buy
from frauk.views.audits import audits
from frauk.views.stats import stats

app.register_blueprint(users)
app.register_blueprint(drinks)
app.register_blueprint(buy)
app.register_blueprint(audits)
app.register_blueprint(stats)
