import datetime
from app import db


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
    fg_color = db.Column(db.String(6), default='f7f9fb')
    bg_color = db.Column(db.String(6), default='56bf8b')

    def fromForm(self,form):
        self.username = form.username.data
        self.email = form.email.data
        self.balance = form.balance.data
        self.audit = form.audit.data
        self.fg_color = form.fg_color.data
        self.bg_color = form.bg_color.data
        self.updated_at = datetime.datetime.now()
