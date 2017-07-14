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
    color = db.Column(db.String(6), default='56bf8b')
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    active = db.Column(db.Boolean)

    def fromForm(self, form):
        self.name = form.name.data
        self.bottle_size_l = form.bottle_size_l.data
        self.caffeine_mg = form.caffeine_mg.data
        self.price = form.price.data
        self.color = form.color.data
        self.updated_at = datetime.datetime.now()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    email = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    balance = db.Column(db.Numeric, default=0)
    active = db.Column(db.Boolean, default=True)
    audit = db.Column(db.Boolean, default=True)
    color = db.Column(db.String(6), default='56bf8b')

    def fromForm(self,form):
        self.username = form.username.data
        self.email = form.email.data
        self.balance = form.balance.data
        self.audit = form.audit.data
        self.color = form.color.data
        self.updated_at = datetime.datetime.now()
