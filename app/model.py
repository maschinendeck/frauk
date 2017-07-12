import datetime
from werkzeug.utils import secure_filename
from app import db, app
import os


class Audit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createt_at = db.Column(db.DateTime, default=datetime.datetime.now())
    difference = db.Column(db.Numeric, default=0)
    drink = db.Column(db.ForeignKey('drink.id'), nullable=False)
    user = db.Column(db.ForeignKey('user.id'), nullable=False)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    bottle_size_l = db.Column(db.Float)
    caffeine_mg = db.Column(db.Integer)
    price = db.Column(db.Numeric)
    logo = db.Column(db.LargeBinary)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    logo_updated_at = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    def __init__(self, name, bottle_size_l, caffeine_mg, price):
        self.name = name
        self.bottle_size_l = bottle_size_l
        self.caffeine_mg = caffeine_mg
        self.price = price

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    email = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    balance = db.Column(db.Numeric, default=0)
    active = db.Column(db.Boolean, default=True)
    audit = db.Column(db.Boolean, default=True)
    logo = db.Column(db.String(250))

    def fromForm(self,form):
        if form.logo.data:
            f = form.logo.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(
                app.root_path, 'static', 'uploads', filename))
            self.logo = filename
        self.username = form.username.data
        self.email = form.email.data
        self.balance = form.balance.data
        self.audit = form.audit.data
        self.updated_at = datetime.datetime.now()
