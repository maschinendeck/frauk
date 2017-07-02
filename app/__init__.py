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

from app.controllers import users, drinks, buy
app.register_blueprint(users)
app.register_blueprint(drinks)
app.register_blueprint(buy)
